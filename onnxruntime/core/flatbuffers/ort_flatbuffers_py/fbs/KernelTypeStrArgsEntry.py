# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class KernelTypeStrArgsEntry(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = KernelTypeStrArgsEntry()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsKernelTypeStrArgsEntry(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def KernelTypeStrArgsEntryBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4F\x52\x54\x4D", size_prefixed=size_prefixed)

    # KernelTypeStrArgsEntry
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # KernelTypeStrArgsEntry
    def KernelTypeStr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # KernelTypeStrArgsEntry
    def Args(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from ort_flatbuffers_py.fbs.ArgTypeAndIndex import ArgTypeAndIndex
            obj = ArgTypeAndIndex()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # KernelTypeStrArgsEntry
    def ArgsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # KernelTypeStrArgsEntry
    def ArgsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def KernelTypeStrArgsEntryStart(builder): builder.StartObject(2)
def Start(builder):
    return KernelTypeStrArgsEntryStart(builder)
def KernelTypeStrArgsEntryAddKernelTypeStr(builder, kernelTypeStr): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(kernelTypeStr), 0)
def AddKernelTypeStr(builder, kernelTypeStr):
    return KernelTypeStrArgsEntryAddKernelTypeStr(builder, kernelTypeStr)
def KernelTypeStrArgsEntryAddArgs(builder, args): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(args), 0)
def AddArgs(builder, args):
    return KernelTypeStrArgsEntryAddArgs(builder, args)
def KernelTypeStrArgsEntryStartArgsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartArgsVector(builder, numElems):
    return KernelTypeStrArgsEntryStartArgsVector(builder, numElems)
def KernelTypeStrArgsEntryEnd(builder): return builder.EndObject()
def End(builder):
    return KernelTypeStrArgsEntryEnd(builder)