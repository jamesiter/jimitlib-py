James Iter's library by python
==============================

建议
----

-  基于各主干的枝叶状态码从50开始，如412主干，则用户自定义枝叶状态码由41250起。

--------------

示例
----

-  枝叶状态码合并

.. code:: python

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

路由器示例
----------

.. code:: python


    from jimit.router import Router, router_table
    from jimit.ji_time import JITime
    import unittest

    reload(sys)
    sys.setdefaultencoding('utf8')

    # 首先配置路由表
    router_table['today'] = JITime.today

    '''
    :param action: 目标路由地址
    :param content: 传给目标的参数内容(content可以是一个字典，这样对于给目标传参更为灵活；示例: {'name': 'James', 'gender': 'M'})
    '''
    print Router.launcher(action='today', content='-')
