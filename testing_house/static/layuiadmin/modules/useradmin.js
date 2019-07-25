/**

 @Name：layuiAdmin 用户管理 管理员管理 角色管理
 @Author：star1029
 @Site：http://www.layui.com/admin/
 @License：LPPL
    
 */


layui.define(['table', 'form'], function(exports){
  var $ = layui.$
  ,table = layui.table
  ,form = layui.form;

  //用户管理
  table.render({
    elem: '#LAY-user-manage'
    ,url: layui.setter.base + 'json/useradmin/webuser.js' //模拟接口
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 100, title: 'ID', sort: true}
      ,{field: 'username', title: '用户名', minWidth: 100}
      ,{field: 'avatar', title: '头像', width: 100, templet: '#imgTpl'}
      ,{field: 'phone', title: '手机'}
      ,{field: 'email', title: '邮箱'}
      ,{field: 'sex', width: 80, title: '性别'}
      ,{field: 'ip', title: 'IP'}
      ,{field: 'jointime', title: '加入时间', sort: true}
      ,{title: '操作', width: 200, align:'center', fixed: 'right', toolbar: '#table-useradmin-webuser'}
    ]]
    ,page: true
    ,limit: 30
    ,height: 'full-220'
    ,text: '对不起，加载出现异常！'
  });
  
  //监听工具条
  table.on('tool(LAY-user-manage)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      layer.prompt({
        formType: 1
        ,title: '敏感操作，请验证口令'
      }, function(value, index){
        layer.close(index);
        
        layer.confirm('真的删除行么', function(index){
          obj.del();
          layer.close(index);
        });
      });
    } else if(obj.event === 'edit'){
      var tr = $(obj.tr);

      layer.open({
        type: 2
        ,title: '编辑用户'
        ,content: '/user_form'
        ,maxmin: true
        ,area: ['500px', '450px']
        ,btn: ['确定', '取消']
        ,yes: function(index, layero){
          var iframeWindow = window['layui-layer-iframe'+ index]
          ,submitID = 'LAY-user-front-submit'
          ,submit = layero.find('iframe').contents().find('#'+ submitID);

          //监听提交
          iframeWindow.layui.form.on('submit('+ submitID +')', function(data){
            var field = data.field; //获取提交的字段
            
            //提交 Ajax 成功后，静态更新表格中的数据
            //$.ajax({});
            table.reload('LAY-user-front-submit'); //数据刷新
            layer.close(index); //关闭弹层
          });  
          
          submit.trigger('click');
        }
        ,success: function(layero, index){
          
        }
      });
    }
  });

  //管理员管理
  layer.load(3);
  table.render({
    elem: '#LAY-user-back-manage'
    ,url: 'user_data'
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 80, title: 'ID', sort: true, align: 'center'}
      ,{field: 'username', width: 100, title: '登录名', align: 'center'}
      ,{field: 'employee_name', width: 100, title: '员工姓名', align: 'center'}
      ,{field: 'sex', width: 100, title: '性别', align: 'center'}
      ,{field: 'job_status', width: 100, title: '在职状态', align: 'center'}
      ,{field: 'role', minWidth: 200, title: '角色', align: 'center'}
      ,{field: 'join_time', minWidth: 100, title: '加入时间', sort: true, align: 'center'}
      ,{title: '操作', minWidth: 300, fixed: 'right', align: 'center', toolbar: '#table-useradmin-admin'}
    ]]
	,page: true
    ,limit: 10
    ,height: 'full-159'
    ,text: '对不起，加载出现异常！'
	,done: function () {
        layer.closeAll('loading');
    }
  });
  //监听工具条
  table.on('tool(LAY-user-back-manage)', function(obj){
      var data = obj.data;
    if(obj.event === 'del'){
      layer.confirm('确定删除用户 "'+ data.username +'" 吗？', {
                        icon: 3
                        ,title: '提示'
                        ,area: ['100%', '160px']
                        ,offset: '0px'
                        ,anim: 1
                        ,btnAlign: 'c'
                    }, function(index){
		$.ajax({
                url: "/user_del",
                type: "GET",
                data: data,
                success: function (msg) {
                    if (msg === '1') {
                        layer.msg("删除成功",{
                                            icon: 1,
                                            offset: '1px',
                                            shift:6,
                                        });
                    } else {
                        layer.msg("删除失败",{
                                            icon: 3,
                                            offset: '1px',
                                            shift:6,
                                        });
                    }
                    layer.load(3);
                    table.reload('LAY-user-back-manage');
                }
            });
        layer.close(index);
      });
    }else if(obj.event === 'reset'){
      layer.confirm('确定重置用户 "'+ data.username +'" 密码吗？', {
                        icon: 3
                        ,title: '提示'
                        ,area: ['100%', '160px']
                        ,offset: '0px'
                        ,anim: 1
                        ,btnAlign: 'c'
                    }, function(index){
		$.ajax({
                url: "/user_reset_password",
                type: "GET",
                data: data,
                success: function (msg) {
                    if (msg === '0') {
                        layer.msg('用户 "' + data.username + '" 密码重置成功',{
                                            icon: 1,
                                            offset: '1px',
                                            shift:6,
                                        });
                    } else {
                        layer.msg('用户 "' + data.username + '" 重置失败!',{
                                            icon: 3,
                                            offset: '1px',
                                            shift:6,
                                        });
                    }
                    layer.load(3);
                    table.reload('LAY-user-back-manage');
                }
            });
        layer.close(index);
      });		
    }else if(obj.event === 'edit'){
      var tr = $(obj.tr);

      layer.open({
        type: 2
        ,title: '编辑'
        ,content: '/user_edit/id=' + data.id
          ,area: ['100%', '560px']
          ,btn: ['保存', '取消']
          ,offset: '0px'
          ,anim: 1
          ,btnAlign: 'c'
        ,yes: function(index, layero){
          var iframeWindow = window['layui-layer-iframe'+ index]
          ,submitID = 'LAY-user-back-submit'
          ,submit = layero.find('iframe').contents().find('#'+ submitID);

          //监听提交
          iframeWindow.layui.form.on('submit('+ submitID +')', function(data){
            var field = data.field; //获取提交的字段
				$.ajax({
					type:'get',
                    url:'/user_edit/id=' + field.id,
                    data: field,
                    success:function(e){
                        if(e==='0'){
                            layer.msg('保存成功',{
                                        icon: 1,
                                        offset: '1px',
                                        shift:6,
                                    });
						} else{
                            layer.msg('保存失败!',{
                                        icon: 2,
                                        offset: '1px',
                                        shift:6,
                                    });
                        }
                        layer.load(3);
                         table.reload('LAY-user-back-manage');
                        }
                    });  
            layer.close(index);
          });  
          
          submit.trigger('click');
        }
        ,success: function(layero, index){           
          
        }
      })
    }
  });

  //角色管理
    layer.load(3);
    table.render({
    elem: '#LAY-user-back-role'
    ,url: 'role_data'
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 80, title: 'ID', sort: true, align: 'center'}
      ,{field: 'name', width:200, title: '角色名称', align: 'center', templet: function (d) {
          return '<a href="javascript:void(0)" lay-event="role_user" style="color: #1E9FFF">'+ d.name +'</a>';}}
      ,{field: 'describe', minWidth:200, title: '角色描述', align: 'center'}
      ,{title: '操作', width: 200, fixed: 'right', align: 'center', toolbar: '#table-role-handle'}
    ]]
	,page: true
    ,limit: 10
    ,height: 'full-80'
    ,text: '对不起，加载出现异常！'
        ,done: function () {
        layer.closeAll('loading');
    }
  });
  
  //监听工具条
  table.on('tool(LAY-user-back-role)', function(obj){
    var data = obj.data;
    if(obj.event === 'del'){
      layer.confirm('确定删除 "' + data.name + '" 角色吗？', {
                        icon: 3
                        ,title: '提示'
                        ,area: ['100%', '160px']
                        ,offset: '0px'
                        ,anim: 1
                        ,btnAlign: 'c'
                    }, function(index){
		$.ajax({
                url: "/role_del",
                type: "GET",
                data: data,
                success: function (msg) {
                    if (msg === '1') {
                        layer.msg("删除成功",{
                                            icon: 1,
                                            offset: '1px',
                                            shift:6,
                                        });
                    } else {
                        layer.msg("删除失败",{
                                            icon: 3,
                                            offset: '1px',
                                            shift:6,
                                        });
                    }
                    layer.load(3);
                    table.reload('LAY-user-back-role');							
                }
            });
        layer.close(index);
      });
    }else if(obj.event === 'edit'){
      var tr = $(obj.tr);

      layer.open({
          type: 2
          , title: '编辑'
          , content: '/role_edit/id=' + data.id
          , area: ['100%', '280px']
          , btn: ['保存', '取消']
          , offset: '0px'
          , anim: 1
          , btnAlign: 'c'
          , yes: function (index, layero) {
              var iframeWindow = window['layui-layer-iframe' + index]
                  , submit = layero.find('iframe').contents().find("#LAY-user-role-submit");

              //监听提交
              iframeWindow.layui.form.on('submit(LAY-user-role-submit)', function (data) {
                  var field = data.field; //获取提交的字段
                  $.ajax({
                      type: 'get',
                      url: '/role_edit/id=' + field.id,
                      data: field,
                      success: function (e) {
                          if (e === '0') {
                              layer.msg('保存成功', {
                                  icon: 1,
                                  offset: '1px',
                                  shift: 6,
                              });
                          } else {
                              layer.msg('保存失败!', {
                                  icon: 2,
                                  offset: '1px',
                                  shift: 6,
                              });
                          }
                          layer.load(3);
                          table.reload('LAY-user-back-role');
                      }
                  });
                  layer.close(index); //关闭弹层
              });
              submit.trigger('click');
          }
      });
    }else if(obj.event === 'role_user'){
      var tr = $(obj.tr);

      layer.open({
        type: 2
        ,title: '人员信息'
        ,content: '/role_user/name=' + data.username
          ,area: ['100%', '280px']
          ,btn: ['保存', '取消']
          ,offset: '0px'
          ,anim: 1
          ,btnAlign: 'c'
        ,yes: function(index, layero) {
              var iframeWindow = window['layui-layer-iframe' + index]
                  , submit = layero.find('iframe').contents().find("#LAY-user-role-submit");

              //监听提交
              iframeWindow.layui.form.on('submit(LAY-user-role-submit)', function (data) {
                  var field = data.field; //获取提交的字段
                  $.ajax({
                      type: 'get',
                      url: '/role_edit/id=' + field.id,
                      data: field,
                      success: function (e) {
                          if (e === '0') {
                              layer.msg('保存成功', {
                                  icon: 1,
                                  offset: '1px',
                                  shift: 6,
                              });
                          } else {
                              layer.msg('保存失败!', {
                                  icon: 2,
                                  offset: '1px',
                                  shift: 6,
                              });
                          }
                          layer.load(3);
                          table.reload('LAY-user-back-role');
                      }
                  });
                  layer.close(index); //关闭弹层
              });
          submit.trigger('click');
        }
        ,success: function(layero, index){
        
        }
      })
    }});
  exports('useradmin', {})
});