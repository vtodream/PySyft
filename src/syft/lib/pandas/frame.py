"""Serde method for pd.DataFrame."""

# third party
import pandas as pd
import pyarrow as pa

# syft relative
from ...generate_wrapper import GenerateWrapper
from ...proto.lib.pandas.frame_pb2 import PandasDataFrame as PandasDataFrame_PB


def object2proto(obj: pd.DataFrame) -> PandasDataFrame_PB:
    """Convert pd.DataFrame to PandasDataFrame_PB with pyarrow.

    Args:
        obj: target dataframe

    Returns:
        Serialized version of Dataframe, which will be used to reconstruct model.

    """
    table = pa.Table.from_pandas(obj)
    return PandasDataFrame_PB(dataframe=pa.serialize(table).to_buffer().to_pybytes())


def proto2object(proto: PandasDataFrame_PB) -> pd.DataFrame:
    """Proto to object conversion using to return desired model.

    Args:
        proto: Serialized version of Dataframe, which will be used to reconstruct model.

    Returns:
        Re-constructed dataframe.
    """
    reconstructed_buf = pa.py_buffer(proto.dataframe)
    return pa.deserialize(reconstructed_buf).to_pandas()


GenerateWrapper(
    wrapped_type=pd.DataFrame,
    import_path="pandas.DataFrame",
    protobuf_scheme=PandasDataFrame_PB,
    type_object2proto=object2proto,
    type_proto2object=proto2object,
)
