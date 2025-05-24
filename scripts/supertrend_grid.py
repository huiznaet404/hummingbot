from typing import Dict
from hummingbot.strategy.script_strategy_base import ScriptStrategyBase, ConnectorBase
import asyncio
import logging
import traceback

class SupertrendGrid(ScriptStrategyBase):
    markets = {
        "bybit_perpetual": ["WIF-USDT"]
    }

    def __init__(self, connectors: Dict[str, ConnectorBase]):
        super().__init__(connectors)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.info("Initializing SupertrendGrid strategy...")

        connector_name = "bybit_perpetual"
        if connector_name not in self.connectors:
            self.logger.error(f"Connector {connector_name} not found!")
            raise ValueError(f"Connector {connector_name} not found!")

        self.bybit_connector = self.connectors[connector_name]
        self.logger.info("Bybit connector initialized successfully.")

    async def start(self, clock, timestamp: float):
        self.logger.info(f"Starting SupertrendGrid strategy at timestamp {timestamp}...")
        try:
            await asyncio.sleep(5)  # Даём время на инициализацию
            self.logger.info("Start method completed successfully.")
        except Exception as e:
            self.logger.error(f"Error in start: {str(e)}\n{traceback.format_exc()}")

    async def tick(self, timestamp: float):
        self.logger.info(f"Tick triggered at timestamp {timestamp}...")
        try:
            self.logger.info("Tick executed successfully.")
        except Exception as e:
            self.logger.error(f"Error in tick: {str(e)}\n{traceback.format_exc()}")

    async def on_stop(self):
        self.logger.info("Stopping SupertrendGrid strategy...")
