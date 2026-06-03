import unittest

from binance_testnet_agent.agent import _balance_total
from binance_testnet_agent.dashboard import _balance_parts


class BalanceAccountingTest(unittest.TestCase):
    def test_dashboard_balance_parts_include_locked_amount(self) -> None:
        balances = {"BTC": {"free": "0.01", "locked": "0.02"}}

        free, locked, total = _balance_parts(balances, "BTC")

        self.assertEqual(free, 0.01)
        self.assertEqual(locked, 0.02)
        self.assertEqual(total, 0.03)

    def test_agent_balance_total_includes_locked_amount(self) -> None:
        balances = {"USDT": {"free": "12.5", "locked": "3.25"}}

        self.assertEqual(_balance_total(balances, "USDT"), 15.75)
