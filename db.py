from dataclasses import dataclass
import sqlite3
import typing as tp


@dataclass
class LockerData:
    locker_id: str
    locked: bool
    passcode: tp.Optional[str]


class DatabaseConnection:
    def __enter__(self) -> sqlite3.Cursor:
        self.connection = sqlite3.connect("db.sqlite3")
        return self.connection.cursor()

    def __exit__(self, *args):
        self.connection.commit()
        self.connection.close()


class Database:
    def __init__(self) -> None:
        with DatabaseConnection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS lockers (
                    locker_id VARCHAR(2) PRIMARY KEY,
                    locked    BOOLEAN    NOT NULL DEFAULT false,
                    passcode  VARCHAR(4)
                );
                """
            )

            for locker_id in ["A1", "A2", "A3", "B1", "B2", "B3"]:
                connection.execute(
                    "INSERT INTO lockers(locker_id) VALUES (?) "
                    "ON CONFLICT DO NOTHING",
                    [locker_id],
                )

    def get_locker(self, locker_id: str) -> tp.Optional[LockerData]:
        with DatabaseConnection() as connection:
            connection.execute(
                "SELECT * FROM lockers WHERE locker_id = ?", [locker_id]
            )
            row = connection.fetchone()

        if row is not None:
            return LockerData(*row)
        return None

    def get_locker_list(self) -> tp.List[LockerData]:
        with DatabaseConnection() as connection:
            connection.execute("SELECT * FROM lockers")
            rows = connection.fetchall()

        return [LockerData(*row) for row in rows]

    def unlock_locker(self, locker_id: str) -> None:
        with DatabaseConnection() as connection:
            connection.execute(
                "UPDATE lockers SET locked = false, passcode = NULL"
                " WHERE locker_id = ?",
                [locker_id],
            )

    def lock_locker(self, locker_id: str, passcode: str) -> None:
        with DatabaseConnection() as connection:
            connection.execute(
                "UPDATE lockers SET locked = true, passcode = ?"
                " WHERE locker_id = ?",
                [passcode, locker_id],
            )

    def reset(self):
        with DatabaseConnection() as connection:
            connection.execute(
                "UPDATE lockers SET locked = false, passcode = NULL"
            )
