import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:genimate/views/text_main.dart';
import 'package:http/http.dart' as http;

import 'breakpoint.dart';

class EmailInputView extends StatefulWidget {
  const EmailInputView({super.key});

  @override
  _EmailInputViewState createState() => _EmailInputViewState();
}

class _EmailInputViewState extends State<EmailInputView> {
  final TextEditingController _emailController = TextEditingController();
  int _isEmailSent = 0; // 이메일 전송 여부를 추적하는 변수 추가

  @override
  void dispose() {
    _emailController.dispose();
    super.dispose();
  }

  Future<void> _sendEmailToServer() async {
    final String email = _emailController.text.trim();
    if (email.isEmpty) {
      return;
    }

    final Uri url = Uri.parse('https://genimate.shop/user/add'); // 서버 URL로 수정
    final Map<String, String> headers = {'Content-Type': 'application/json'};
    final Map<String, String> body = {'email': email};

    final http.Response response = await http.post(
      url,
      headers: headers,
      body: json.encode(body),
    );

    if (response.statusCode == 201) {
      // 이메일 전송 성공
      setState(() {
        _isEmailSent = 1;
      });
    } else if (response.statusCode == 400) {
      setState(() {
        _isEmailSent = -1;
      });
    } else {
      // 이메일 전송 실패
      setState(() {
        _isEmailSent = 0;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final scaffoldMessenger = ScaffoldMessenger.of(context);
    final double currenWidth = MediaQuery.of(context).size.width;
    var isWeb = currenWidth > BreakPoint.mobile ? true : false;
    String buttonText;
    if (_isEmailSent != 0) {
      buttonText = '돌아가기';
    } else {
      buttonText = '신청하기';
    }
    final buttonStyle = ElevatedButton.styleFrom(
      backgroundColor: const Color.fromRGBO(239, 59, 54, 1),
      padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 15),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(7),
      ),
      shadowColor: Colors.black12,
    );

    return Scaffold(
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const MainText(),
              SizedBox(
                height: 400,
                width: 400,
                child: Center(
                  child: TextField(
                    controller: _emailController,
                    decoration: const InputDecoration(
                        labelText: 'Email Address',
                        labelStyle: TextStyle(fontSize: 20)),
                  ),
                ),
              ),
              const SizedBox(height: 15),
              ElevatedButton(
                onPressed: () async {
                  if (buttonText == '신청하기') {
                    await _sendEmailToServer();
                  }

                  if (buttonText == '돌아가기') {
                    Navigator.pushNamed(context, '/');
                  }
                },
                style: buttonStyle,
                child: Text(
                  buttonText,
                  style: const TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w300,
                  ),
                ),
              ),
              if (_isEmailSent > 0) // _isEmailSent가 true인 경우에만 Text 표시
                const Text(
                  '이메일이 성공적으로 전송되었습니다.',
                  style: TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.w500,
                    color: Colors.black87, // 텍스트 색상은 원하는 대로 설정 가능
                  ),
                ),
              if (_isEmailSent < 0) // _isEmailSent가 true인 경우에만 Text 표시
                const Text(
                  '이미 존재하는 이메일 입니다.',
                  style: TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.w500,
                    color: Colors.black87, // 텍스트 색상은 원하는 대로 설정 가능
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
