"""Layar kalender bulanan + indikator & detail tanggal (F005)."""

import calendar
from datetime import date

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem

from controllers.calendar_controller import CalendarController


class CalendarScreen(Screen):
    """Kalender bulanan dengan agregasi notes/todos."""

    def __init__(self, **kwargs):
        """Siapkan controller & bulan aktif."""
        super().__init__(**kwargs)
        self.cal_ctrl = CalendarController()
        today = date.today()
        self.current_year = today.year
        self.current_month = today.month

    def on_enter(self, *args) -> None:
        """Render header bulan."""
        Clock.schedule_once(self.refresh_header, 0.1)

    def refresh_header(self, dt=None) -> None:
        """Perbarui label bulan aktif.

        Args:
            dt: Delta dari Clock (opsional).
        """
        month_name = calendar.month_name[self.current_month]
        self.ids.month_label.text = f"{month_name} {self.current_year}"

    def prev_month(self) -> None:
        """Navigasi bulan sebelumnya."""
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.refresh_header()

    def next_month(self) -> None:
        """Navigasi bulan berikutnya."""
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.refresh_header()

    def show_day_detail(self, day: int) -> None:
        """Tampilkan notes & todos pada tanggal tertentu.

        Args:
            day (int): Tanggal dalam bulan aktif.
        """
        date_str = f"{self.current_year:04d}-{self.current_month:02d}-{day:02d}"
        result = self.cal_ctrl.get_events_by_date(date_str)

        container = self.ids.day_detail_container
        container.clear_widgets()
        if not result["success"]:
            return

        for note in result["data"]["notes"]:
            container.add_widget(OneLineListItem(text=f"📝 {note['title']}"))
        for todo in result["data"]["todos"]:
            mark = "✅" if todo["is_done"] else "⬜"
            container.add_widget(OneLineListItem(text=f"{mark} {todo['task']}"))
