import jsonpath

class CheckpointBuilder(object):
    failureException = AssertionError

    def __init__(self):
        # 方法字典
        self._type_equality_funcs = {
            "assertEqual": "_assertEqual",
            'assertNotEqual': 'assertNotEqual',
            'assertIn': 'assertIn',
            'assertNotIn': 'assertNotIn'
        }

    def run(self, func, first, second, msg=None):
        # 校验的对象都转成字符串
        first, second = str(first), str(second)
        # 根据设置的枚举选择并获取方法
        assertion_func = self._getAssertFunc(func)
        assertion_func(first, second, msg=msg)

    def _getAssertFunc(self, func):
        """根据字典获取对应的方法"""
        asserter = self._type_equality_funcs.get(func)
        if asserter is not None:
            if isinstance(asserter, str):
                asserter = getattr(self, asserter)
            return asserter
        # 不是统一数据类型返回默认验证方法
        return self._baseAssertEqual

    def _baseAssertEqual(self, first, second, msg=None):
        """默认校验方法"""
        if not first == second:
            raise self.failureException(msg)

    def _assertEqual(self, first, second, msg=None):
        """判断值相等"""
        return first == second

    def _assertNotEqual(self, first, second, msg=None):
        """判断值不想等"""
        return first != second

    def _assertIn(self, first, second, msg=None):
        """判断包含"""
        pass

    def _assertNotIn(self, first, second, msg=None):
        """判断不包含"""
        pass


if __name__ == '__main__':
    a = '{"a": "u6d4bu8bd51", "b": "u6d4bu8bd52"}'
    jsonpath.jsonpath('$..',)