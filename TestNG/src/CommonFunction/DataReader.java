package CommonFunction;
import org.w3c.dom.*;
public class DataReader {
/**
* ��Xml�л�ȡ��Ӧ�Ľڵ������
* @param doc �����ļ���Document
* @param firsttag �ӽڵ�
* @param secondtag Ҫ��ȡ��Ԫ�صĽڵ�
* @return Ҫ���ҵĽڵ�����
*/
	public String readnodevalue(Document doc,String firsttag,String secondtag)
	{
		String result="";
		Element root=doc.getDocumentElement();
		NodeList childnode = root.getElementsByTagName(firsttag);
		NodeList resnode=childnode.item(0).getChildNodes();
		for(int i=0;i<resnode.getLength();i++)
		{
			if(resnode.item(i).getNodeName().equals(secondtag))
			{
				result=resnode.item(i).getTextContent();
				break;
			}
		}
		return result;
	}
}