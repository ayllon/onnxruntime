# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Attribute(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Attribute()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAttribute(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    @classmethod
    def AttributeBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4F\x52\x54\x4D", size_prefixed=size_prefixed)

    # Attribute
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Attribute
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Attribute
    def DocString(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Attribute
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Attribute
    def F(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Attribute
    def I(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # Attribute
    def S(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Attribute
    def T(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from ort_flatbuffers_py.fbs.Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Attribute
    def G(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from ort_flatbuffers_py.fbs.Graph import Graph
            obj = Graph()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Attribute
    def Floats(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Attribute
    def FloatsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # Attribute
    def FloatsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def FloatsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        return o == 0

    # Attribute
    def Ints(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # Attribute
    def IntsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # Attribute
    def IntsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def IntsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # Attribute
    def Strings(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Attribute
    def StringsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def StringsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # Attribute
    def Tensors(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from ort_flatbuffers_py.fbs.Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Attribute
    def TensorsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def TensorsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        return o == 0

    # Attribute
    def Graphs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from ort_flatbuffers_py.fbs.Graph import Graph
            obj = Graph()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Attribute
    def GraphsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Attribute
    def GraphsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        return o == 0

def AttributeStart(builder): builder.StartObject(13)
def Start(builder):
    return AttributeStart(builder)
def AttributeAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return AttributeAddName(builder, name)
def AttributeAddDocString(builder, docString): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(docString), 0)
def AddDocString(builder, docString):
    return AttributeAddDocString(builder, docString)
def AttributeAddType(builder, type): builder.PrependInt32Slot(2, type, 0)
def AddType(builder, type):
    return AttributeAddType(builder, type)
def AttributeAddF(builder, f): builder.PrependFloat32Slot(3, f, 0.0)
def AddF(builder, f):
    return AttributeAddF(builder, f)
def AttributeAddI(builder, i): builder.PrependInt64Slot(4, i, 0)
def AddI(builder, i):
    return AttributeAddI(builder, i)
def AttributeAddS(builder, s): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(s), 0)
def AddS(builder, s):
    return AttributeAddS(builder, s)
def AttributeAddT(builder, t): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(t), 0)
def AddT(builder, t):
    return AttributeAddT(builder, t)
def AttributeAddG(builder, g): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(g), 0)
def AddG(builder, g):
    return AttributeAddG(builder, g)
def AttributeAddFloats(builder, floats): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(floats), 0)
def AddFloats(builder, floats):
    return AttributeAddFloats(builder, floats)
def AttributeStartFloatsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartFloatsVector(builder, numElems):
    return AttributeStartFloatsVector(builder, numElems)
def AttributeAddInts(builder, ints): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(ints), 0)
def AddInts(builder, ints):
    return AttributeAddInts(builder, ints)
def AttributeStartIntsVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def StartIntsVector(builder, numElems):
    return AttributeStartIntsVector(builder, numElems)
def AttributeAddStrings(builder, strings): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(strings), 0)
def AddStrings(builder, strings):
    return AttributeAddStrings(builder, strings)
def AttributeStartStringsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartStringsVector(builder, numElems):
    return AttributeStartStringsVector(builder, numElems)
def AttributeAddTensors(builder, tensors): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(tensors), 0)
def AddTensors(builder, tensors):
    return AttributeAddTensors(builder, tensors)
def AttributeStartTensorsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartTensorsVector(builder, numElems):
    return AttributeStartTensorsVector(builder, numElems)
def AttributeAddGraphs(builder, graphs): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(graphs), 0)
def AddGraphs(builder, graphs):
    return AttributeAddGraphs(builder, graphs)
def AttributeStartGraphsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartGraphsVector(builder, numElems):
    return AttributeStartGraphsVector(builder, numElems)
def AttributeEnd(builder): return builder.EndObject()
def End(builder):
    return AttributeEnd(builder)