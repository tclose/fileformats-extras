import typing as ty
import pydicom
from fileformats.core import FileSet
from fileformats.application import Dicom


@FileSet.read_metadata.register
def dicom_read_metadata(dicom: Dicom, specific_tags=None) -> ty.Mapping[str, ty.Any]:
    dcm = pydicom.dcmread(dicom.fspath, specific_tags=specific_tags)
    [getattr(dcm, a) for a in dir(dcm)]  # Ensure all keywords are set
    metadata = {
        e.keyword: e.value  # type: ignore[union-attr]
        for e in dcm.elements()
        if getattr(e, "keyword", False) and e.keyword != "PixelData"  # type: ignore[union-attr]
    }
    return metadata
