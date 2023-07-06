# relative
from ..serde.serializable import serializable
from .client import SyftClient


@serializable()
class GatewayClient(SyftClient):
    def __repr__(self) -> str:
        return f"<GatewayClient: {self.name}>"
