#coding:GBK
import smtplib
from email.mime.text import MIMEText

Host = 'mail1.oa.cebbank.com'
SubJect = '����������'
TO = 'nas@cebbank.com'
From = 'nas@cebbank.com'
msg = MIMEText("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>����-�й��������</title>
<meta  name="ҳ������ʱ��" content="2016-03-24 10:55:11" />
<meta  name="��������ʱ��" content="2016-01-21 19:40:28"/>
<meta name="keywords" content="  " />
<meta name="description" content=" ����  " />
<link rel="stylesheet" type="text/css" media="screen" href="/site/uiFramework/huilan-jquery-ui/css/huilan-jquery-ui.css" />
<script type="text/javascript" src="/site/uiFramework/huilan-jquery-ui/js/huilan-jquery-ui.js?self=true&skin=default"></script>
 <META NAME="WT.cg_ceb" CONTENT="/����ҵ��/�ۺ�Ƶ��//">  </head>
 <body>
  <link rel="stylesheet" type="text/css" media="screen" href="/site/template/site.css" />
  <script type="text/javascript" src="/site/template/site.js"></script><div style="display:none" easysite="easysiteHiddenDiv">
	<input id="contextPath" value="/eportal" type="hidden"/>
	<input id="isOnlyUseCkeditorSourceMode" value="$isOnlyUseCkeditorSourceMode" type="hidden"/>
	<input id="eprotalCurrentPageId" value="490793" type="hidden"/>
	<input id="eprotalCurrentSiteId" value="458135" type="hidden"/>
	<input id="eprotalCurrentArticleKey"  value=""  type="hidden"/>
	<input id="eprotalCurrentColumnId"  value=""  type="hidden"/>
	<input id="isStaticRequest" value="yes" type="hidden"/>
	<input id="isOpenStaticPageList" value="" type="hidden"/>
	<input id="defaultPublishPage" value="3" type="hidden"/>
	<input type='hidden' id='eportalappPortletId' value="3">
	<input type='hidden' id='epsPortletId' value="1">
	<script type="text/javascript" src="/site/uiFramework/js/counting/chanelCounting.js"></script>
	<input type="hidden" id="ckEditorUploadFileUrl" value="/eportal/ui?moduleId=2&pageId=490793&struts.portlet.action=/portlet/uploadFile.action&isCkEditor=true"/>
	<input type="hidden" id="sDtoLoginUrl" value="moduleId=3&pageId=490793&struts.portlet.action=/app/member!sDtoLogin.action"/>
	<input type="hidden" id="memberLoginUrl" value="/eportal/ui?moduleId=3&pageId=490793&struts.portlet.action=/app/member!toLogin.action"/>
	<input type="hidden" id="currentLoginMemberId"  value="" />
	<input type="hidden" id="currentLoginMemberName"  value="" />
	<input type="hidden" id="behaviourAnalysisSiteId"  value="" />
	<input type="hidden" id="isOpenArticleScan" value="no"/>
		<input type="hidden" id="voteUrl" value="/eportal/ui?moduleId=1&pageId=490793&struts.portlet.action=/portlet/article!vote.action"/>
	<input type="hidden" id="getVoteCount" value="/eportal/ui?moduleId=1&pageId=490793&struts.portlet.action=/portlet/article!getVoteCount.action"/>
	<input type="hidden" id="getHotWordRelativeArticle" value="/eportal/ui?moduleId=1&pageId=490793&struts.portlet.action=/portlet/article!getHotWordRelativeArticle.action&staticRequest=yes"/>
	<input type="hidden" id="deleteArticleUrl" value="/eportal/ui?moduleId=1&pageId=490793&struts.portlet.action=/portlet/article!deleteArticle.action"/>
	<input type="hidden" id="toSnsLoginUrl" value="/eportal/ui?moduleId=3&pageId=490793&struts.portlet.action=/app/member-sns-login!toSnsLogin.action"/>
	<input type="hidden" id="portalLastRequestUrl"  value="" />
</div>  <div class="sozc column" id="sozcpane" name="neirong" runat="server">
     <div class="portlet" id="13313">
 <div align="left" class="portlet-header">
  <span id="menu">
        </span>
  <div id="submenu13313" class="shadow dn">
   <ul class="float_list_ul">
        </ul>
  </div>
 </div>
 <div>
   <div class="sy_gg"><p class="p1">�𾴵Ŀͻ���</p>
<p class="p2">����֣����ʾ����߷��շ�����ʶ���������Լ��������û�������¼���롢��������/�ֻ���̬���뼰���������˽����Ϣ����Ҫ������Դ�����Ķ��š��ʼ��͵绰���ڵ�¼��������ʱ�������ֹ������й�������йٷ���ַ<a href="http://www.cebbank.com" target="_blank">www.cebbank.com</a>���������������е�<strong>Ԥ����Ϣ</strong>����Ҫͨ����������Ȳ�����ַ���ӵ�¼��������¼������վ�ϵ���ƭ��</p>
<p class="p3">�й��������</p>
</div>
<style type="text/css">
.sy_gg{
   width:529px;
   height:521px;
   background:url(/static/cebbank/images/pic/sy_gg_bg.jpg) no-repeat;
}
.sy_gg .p1{
   padding-top:138px;
   padding-left:40px;
   font-size:14px;
   font-family:"΢���ź�";
   color:#565050;
}
.sy_gg .p2{
   padding-left:40px;
   padding-right:47px;
   padding-top:10px;
   font-size:14px;
   font-family:"΢���ź�";
   color:#565050;
   line-height:32px;
   text-indent:28px;
}
.sy_gg .p2 a{
   color:blue;
   text-decoration:underline;
   font-weight:bold;
   font-size:14px;
}
.sy_gg .p2 strong{
   color:#3e3838;
   font-size:14px;
}
.sy_gg .p3{
   text-align:right;
   padding-right:50px;
   padding-top:10px;
   font-family:"΢���ź�";
   font-size:14px;
   color:#565050;
}</style>


 </div>
</div>   </div>
  <style type="text/css">
*{
	padding:0;
	margin:0;
}
.sozc{
	width:149px;
}
</style><div style="display:none" easysite="easysiteHiddenDiv">
<input type="hidden"  id="currentLoginUserLoginName"/>
</div> </body>
</html>
""","Html","UTF-8")

msg['Subject'] = SubJect
msg['From'] = From
msg['To'] = TO
try:
    server = smtplib.SMTP()
    server.connect(Host,'25')
    server.login("nas","password")
    print('111')
    server.sendmail(From,TO,msg.as_string())
    print('222')
    server.quit()
    print("���ͳɹ�")
except Exception as e:
    print("����ʧ��"+str(e))

