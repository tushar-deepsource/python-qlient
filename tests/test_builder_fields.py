def test_fields_simple_single():
    from qlient.builder import Fields, Field
    a = Fields("a")
    assert a.fields == [Field("a")]


def test_fields_simple_multiple():
    from qlient.builder import Fields, Field
    a = Fields("a", "b", "c")
    assert Field("a") in a.fields
    assert Field("b") in a.fields
    assert Field("c") in a.fields


def test_fields_simple_multiple_duplicates():
    from qlient.builder import Fields
    a = Fields("a", "b", "c", "c", "c")
    assert len(a.fields) == 3


def test_fields_simple_list():
    from qlient.builder import Fields, Field
    a = Fields(["a", "b", "c"])
    assert Field("a") in a.fields
    assert Field("b") in a.fields
    assert Field("c") in a.fields


def test_fields_simple_list_duplicates():
    from qlient.builder import Fields
    fields = ["a", "b", "c", "c", "c"]
    a = Fields(fields)
    assert len(a.fields) == 3


def test_fields_complex_simple():
    from qlient.builder import Fields, Field
    a = Fields("a", "b", c="d")
    assert Field("a") in a.fields
    assert Field("b") in a.fields
    assert Field("c", _sub_fields=Fields("d")) in a.fields


def test_fields_complex_simple_list():
    from qlient.builder import Fields, Field
    a = Fields("a", "b", c=["a", "b"])
    assert Field("a") in a.fields
    assert Field("b") in a.fields
    assert Field("c", _sub_fields=Fields("a", "b")) in a.fields


def test_fields_complex_nested_fields():
    from qlient.builder import Fields, Field
    a = Fields(a=Fields("a"), b=Fields("b"))
    assert Field("a", _sub_fields="a") in a.fields
    assert Field("b", _sub_fields="b") in a.fields


def test_fields_simple_eq_operator():
    from qlient.builder import Fields
    a = Fields("a")
    b = Fields("a")
    assert a == b


def test_fields_simple_eq_operator_not():
    from qlient.builder import Fields
    a = Fields("a")
    b = Fields("b")
    assert a != b


def test_fields_complex_eq_operator():
    from qlient.builder import Fields
    a = Fields("a", b="c")
    b = Fields("a", b="c")
    assert a == b


def test_fields_complex_eq_operator_not():
    from qlient.builder import Fields
    a = Fields("a", b="c")
    b = Fields("a", b="d")
    assert a != b


def test_fields_simple_add_operator_simple():
    from qlient.builder import Fields
    a = Fields("a")
    expected = Fields("a", "b")
    actual = a + "b"
    assert expected == actual


def test_fields_simple_add_operator_list():
    from qlient.builder import Fields
    a = Fields("a")
    expected = Fields("a", "b", "c")
    actual = a + ["b", "c"]
    assert expected == actual


def test_fields_simple_add_operator_dict():
    from qlient.builder import Fields
    a = Fields("a")
    expected = Fields("a", b="c")
    actual = a + {"b": "c"}
    assert expected == actual


def test_fields_simple_add_operator_fields():
    from qlient.builder import Fields
    a = Fields("a")
    b = Fields("a", "b", c="d")
    expected = Fields("a", "b", c="d")
    actual = a + b
    assert expected == actual


def test_fields_complex_add_operator_simple():
    from qlient.builder import Fields, Field
    a = Fields("a", b="b")
    actual = a + "c"
    assert Field("a") in actual.fields
    assert Field("b", _sub_fields="b") in actual.fields
    assert Field("c") in actual.fields


def test_fields_complex_add_operator_list():
    from qlient.builder import Fields, Field
    a = Fields("a", b="b")
    actual = a + ["a", "c", "z"]
    assert Field("a") in actual.fields
    assert Field("b", _sub_fields="b") in actual.fields
    assert Field("c") in actual.fields
    assert Field("z") in actual.fields


def test_fields_complex_add_operator_dict():
    from qlient.builder import Fields, Field
    a = Fields("a", b="b")
    actual = a + {"b": ["c", "e"]}
    assert Field("a") in actual.fields
    assert Field("b", _sub_fields=["c", "e"]) in actual.fields


def test_fields_complex_add_operator_fields():
    from qlient.builder import Fields, Field
    a = Fields("a", b="b")
    b = Fields("a", "c")
    actual = a + b
    assert Field("a") in actual.fields
    assert Field("c") in actual.fields
    assert Field("b", _sub_fields="b") in actual.fields
