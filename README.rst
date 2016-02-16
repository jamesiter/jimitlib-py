James Iter's library by python
==============================

添加自定义状态码示例
--------------------

-  枝叶状态码合并

.. code:: python

    import jimit as ji

    own_state_branch = {
            '41250': {
                'code': '41250',
                'zh-cn': '账密不匹配'
                }
            }
            
    ji.state_code.index_state['branch'] = dict(ji.state_code.index_state['branch'], **own_state_branch)
    print json.dumps(ji.Commons.exchange_state(41250), ensure_ascii=False)

    {
        "code": "412",
        "zh-cn": "先决条件失败",
        "en-us": "Precondition Failed",
        "sub": {
            "zh-cn": "账密不匹配",
            "code": "41250"
        }
    }

自定义状态码建议
----------------

-  基于各主干的枝叶状态码从50开始，如412主干，则用户自定义枝叶状态码由41250起。

--------------

路由器示例
----------

.. code:: python


    from jimit.router import Router, router_table
    from jimit.ji_time import JITime
    import unittest

    reload(sys)
    sys.setdefaultencoding('utf8')

    '''
    首先配置路由表
    '''
    router_table['today'] = JITime.today

    '''
    :param action: 目标路由地址
    :param content: 传给目标的参数内容(content可以是一个字典，这样对于给目标传参更为灵活；示例: {'name': 'James', 'gender': 'M'})
    '''
    print Router.launcher(action='today', content='-')

--------------

类型判断示例
------------

参数说明
~~~~~~~~

.. code:: python

    args_rules = [
        (类型[int|long|str|basestring|list|dict...](必须), 变量名(必须), 取值范围(可选), 必须存在(可选,默认为True))
    ]
    取值范围: 列表为枚举['male', 'female', 'other'], 元组为起止范围(10, 100)
    必须存在: 布尔值,默认为True, 当该值为True时,则表示该变量必须存在; 否则,仅当该变量存在时,才匹配该条策略

    args = {
        '变量名': 变量值
    }

    try:
        ji.Check.previewing(args_rules, args)
    except ji.PreviewingError, e:
        ret = json.loads(e.message)
        异常处理域

示例1
~~~~~

.. code:: python

    状态码200为正常,其它都为异常
    详细描述在ret['state']['sub']中
    异常会于PreviewingError类型抛出,可通过json.loads(e.message)来结构化异常描述
    更多异常用法请移步参考:
    https://github.com/jamesiter/jimitlib-py/blob/master/tests/test_check.py

    import jimit as ji

    form_rules = [
        (int, 'k', (10, 100))
    ]

    form = {
        'k': 10
    }

    assert '200' == ji.Check.previewing(form_rules, form)['state']['code'])

示例2
~~~~~

.. code:: python

    form_rules = [
        (str, 'k')
    ]

    form = {
        'k': 123
    }

    try:
        ji.Check.previewing(form_rules, form)
    except ji.PreviewingError, e:
        ret = json.loads(e.message)
        
    assert '41202' == ret['state']['sub']['code']
