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
  layer.load(3);
  table.render({
      elem: '#LAY-user-back-manage'
      ,skin: 'line'
      ,size: 'sm'
      ,url: '/user_data'
      ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 80, title: 'ID', sort: true, align: 'center', fixed: 'left'}
      ,{field: 'username', width: 100, title: '登录名', align: 'center', fixed: 'left'}
      ,{field: 'employee_name', width: 100, title: '员工姓名', align: 'center'}
      ,{field: 'sex', width: 100, title: '性别', align: 'center'}
      ,{field: 'job_status', width: 100, title: '在职状态', align: 'center'}
      ,{field: 'role', minWidth: 100, title: '角色', align: 'center'}
      ,{field: 'department', minWidth: 100, title: '部门', align: 'center'}
      ,{field: 'jobs_name', minWidth: 100, title: '岗位', align: 'center'}
      ,{field: 'join_time', minWidth: 100, title: '加入时间', sort: true, align: 'center'}
      ,{field: 'locking', title:'是否锁定', width:110, unresize: true, fixed: 'right',
              templet: function (d) {
                  if (d.locking === 1){
                      return '<input type="checkbox" title="锁定" checked>'}
                  else{
                      return '<input type="checkbox" title="锁定">'}
                  }
          }
      ,{title: '操作', width: 120, fixed: 'right', align: 'center', toolbar: '#table-useradmin-admin'}
      ]]
	  ,page: true
      ,limit: 10
      ,height: 'full-150'
      ,text: '对不起，加载出现异常！'
	  ,done: function () {
          layer.closeAll('loading');
      }
  });
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
                        layer.confirm('用户 "' + data.username + '" 密码重置成功 默认密码为 "eLTE@com123" 请及时修改密码！',{
                                    icon: 1
                                    ,title: '提示'
                                    ,area: ['100%', '160px']
                                    ,offset: '0px'
                                    ,anim: 1
                                    ,btnAlign: 'c'
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
        var old_name = data.username;
      layer.open({
        type: 2
        ,title: '编辑'
        ,content: '/user_edit/name=' + old_name
          ,area: ['100%', '520px']
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
                    url:'/user_edit/name=' + old_name,
                    data: field,
                    success:function(e){
                        if(e==='0'){
                            layer.close(index);
                            layer.msg('保存成功',{
                                        icon: 1,
                                        offset: '1px',
                                        shift:6,
                                    });
						}else if (e === '1'){
                            layer.msg('用户已存在!',{
                                        icon: 2,
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
        ,url: '/role_data'
        ,skin: 'line'
        ,size: 'sm'
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
        ,height: 'full-90'
        ,text: '对不起，加载出现异常！'
        ,done: function () {
        layer.closeAll('loading');
        }
    });
  
  //监听工具条
  table.on('tool(LAY-user-back-role)', function(obj) {
      var data = obj.data;
      if (obj.event === 'del') {
          layer.confirm('确定删除 "' + data.name + '" 角色吗？', {
              icon: 3
              , title: '提示'
              , area: ['100%', '160px']
              , offset: '0px'
              , anim: 1
              , btnAlign: 'c'
          }, function (index) {
              $.ajax({
                  url: "/role_del",
                  type: "GET",
                  data: data,
                  success: function (msg) {
                      if (msg === '1') {
                          layer.msg("删除成功", {
                              icon: 1,
                              offset: '1px',
                              shift: 6,
                          });
                      } else {
                          layer.msg("删除失败", {
                              icon: 3,
                              offset: '1px',
                              shift: 6,
                          });
                      }
                      layer.load(3);
                      table.reload('LAY-user-back-role');
                  }
              });
              layer.close(index);
          });
      } else if (obj.event === 'edit') {
          var tr = $(obj.tr);
          var old_name = data.name;

          layer.open({
              type: 2
              , title: '编辑'
              , content: '/role_edit/name=' + old_name
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
                          url: '/role_edit/name=' + old_name,
                          data: field,
                          success: function (e) {
                              if (e === '0') {
                                  layer.close(index);
                                  layer.msg('保存成功', {
                                      icon: 1,
                                      offset: '1px',
                                      shift: 6,
                                  });
                              }else if (e === '1'){
                                  layer.msg('角色已存在!', {
                                      icon: 2,
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
                  });
                  submit.trigger('click');
              }
          });
      } else if (obj.event === 'role_user') {
          var tr = $(obj.tr);

          layer.open({
              type: 2
              , title: '人员信息'
              , content: '/role_user/name=' + data.username
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
              , success: function (layero, index) {

              }
          });
      }
  });

  //小组管理
    layer.load(3);
    table.render({
    elem: '#LAY-group-manage'
    ,url: '/group_data'
    ,skin: 'line'
    ,size: 'sm'
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 80, title: 'ID', sort: true, align: 'center'}
      ,{field: 'name', width:200, title: '小组名称', align: 'center'}
      ,{field: 'describe', minWidth:200, title: '小组描述', align: 'center'}
      ,{title: '操作', width: 200, fixed: 'right', align: 'center', toolbar: '#table-role-handle'}
    ]]
	,page: true
    ,limit: 10
    ,height: 'full-90'
        ,done: function () {
        layer.closeAll('loading');
    }
  });

  //监听工具条
  table.on('tool(LAY-group-manage)', function(obj) {
      var data = obj.data;
      if (obj.event === 'group_edit') {
          var tr = $(obj.tr);
          var old_name = data.name
          layer.open({
              type: 2
              , title: '编辑'
              , content: '/group_edit/name=' + old_name
              , area: ['100%', '280px']
              , btn: ['保存', '取消']
              , offset: '0px'
              , anim: 1
              , btnAlign: 'c'
              , yes: function (index, layero) {
                  var iframeWindow = window['layui-layer-iframe' + index]
                      , submit = layero.find('iframe').contents().find("#LAY-group-edit-submit");

                  //监听提交
                  iframeWindow.layui.form.on('submit(LAY-group-edit-submit)', function (data) {
                      var field = data.field; //获取提交的字段
                      $.ajax({
                          type: 'get',
                          url: '/group_edit/name=' + old_name,
                          data: field,
                          success: function (e) {
                              if (e === '0') {
                                  layer.close(index);
                                  layer.msg('保存成功', {
                                      icon: 1,
                                      offset: '1px',
                                      shift: 6,
                                  });
                              }else if (e === '1') {
                                  layer.msg('小组已存在!', {
                                      icon: 2,
                                      offset: '1px',
                                      shift: 6,
                                  });
                              }else {
                                  layer.msg('保存失败!', {
                                      icon: 2,
                                      offset: '1px',
                                      shift: 6,
                                  });
                              }
                              layer.load(3);
                              table.reload('LAY-group-manage');
                          }
                      });
                  });
                  submit.trigger('click');
              }
          });
      }
  });

  //岗位管理
    layer.load(3);
    table.render({
    elem: '#LAY-jobs-manage'
    ,url: '/jobs_data'
    ,skin: 'line'
    ,size: 'sm'
    ,cols: [[
      {type: 'checkbox', fixed: 'left'}
      ,{field: 'id', width: 80, title: 'ID', sort: true, align: 'center'}
      ,{field: 'name', width:200, title: '岗位名称', align: 'center'}
      ,{field: 'describe', minWidth:200, title: '岗位描述', align: 'center'}
      ,{title: '操作', width: 200, fixed: 'right', align: 'center', toolbar: '#table-jobs-handle'}
    ]]
	,page: true
    ,limit: 10
    ,height: 'full-90'
        ,done: function () {
        layer.closeAll('loading');
    }
  });

  //监听工具条
  table.on('tool(LAY-jobs-manage)', function(obj) {
      var data = obj.data;
        if (obj.event === 'jobs_edit') {
          var tr = $(obj.tr);
          var old_name = data.name;

          layer.open({
              type: 2
              , title: '编辑'
              , content: '/jobs_edit/name=' + old_name
              , area: ['100%', '280px']
              , btn: ['保存', '取消']
              , offset: '0px'
              , anim: 1
              , btnAlign: 'c'
              , yes: function (index, layero) {
                  var iframeWindow = window['layui-layer-iframe' + index]
                      , submit = layero.find('iframe').contents().find("#LAY-jobs-edit-submit");

                  //监听提交
                  iframeWindow.layui.form.on('submit(LAY-jobs-edit-submit)', function (data) {
                      var field = data.field; //获取提交的字段
                      $.ajax({
                          type: 'get',
                          url: '/jobs_edit/name=' + old_name,
                          data: field,
                          success: function (e) {
                              if (e === '0') {
                                  layer.close(index);
                                  layer.msg('保存成功', {
                                      icon: 1,
                                      offset: '1px',
                                      shift: 6,
                                  });
                              }else if (e === '1'){
                                  layer.msg('岗位已存在！', {
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
                              table.reload('LAY-jobs-manage');
                          }
                      });
                  });
                  submit.trigger('click');
              }
          });
      }
  });

  exports('useradmin', {})
});
