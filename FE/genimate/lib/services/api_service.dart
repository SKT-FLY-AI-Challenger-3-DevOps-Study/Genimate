import 'dart:convert';

import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl = "http://211.57.200.6:8000";
  final String user = "user/add";
  var data = "";

  void postGenimate() async {
    final url = Uri.parse('$baseUrl/$user');
    final response = await http.post(
      url,
      headers: {
        'Content-Type': 'application/json', // JSON 형식으로 데이터를 보내기 위해 헤더 설정
      },
      body: jsonEncode(data), // 데이터를 JSON 형식으로 인코딩하여 body에 추가
    );
    if (response.statusCode == 200) {
      print(response.body);
    }
    throw Error();
  }
}


