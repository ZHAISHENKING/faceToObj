# GET请求，获取交易记录代码片段
"""
按get请求的args参数给出返回值
"""

class SearchLog(Resource):
    """
    :param: log_id
    """
    @catch_exception
    @jwt_required
    @super
    def get(self):
        data = request.args
        log = PaymentLog.objects.all()

        # 按id查询
        id = data.get("id")
        if id:
            log = log.filter(id=ObjectId(id))

        # 按课程名查询
        course = data.get("course")
        if course:
            log = log.filter(course__icontains=course)

        # 按创建人查询
        create_by = data.get("create_by")
        if create_by:
            user = User.objects.filter(Q(name__icontains=create_by) | Q(phone__icontains=create_by))
            log = log.filter(user__in=user)

        result = []
        for i in log:
            obj = dict({
                "id": str(i["id"]),
                "user": i["user"].name,
                "channel": i["channel"],
                "created_at": TimeFomat().ms(i["created_at"]),
                "course": i["course"],
                "status": i["status"],
                "amount_paid": i["amount_paid"]
            })
            result.append(obj)
        return trueReturn(result)
