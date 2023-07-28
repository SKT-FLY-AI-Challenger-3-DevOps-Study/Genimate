import 'package:flutter/material.dart';
import 'package:genimate/views/email_view.dart';
import 'package:genimate/views/home_view.dart';

void main() {
  runApp(const Genimate());
}

class Genimate extends StatelessWidget {
  const Genimate({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        fontFamily: "NotoSansKR",
        primaryColor: const Color.fromARGB(255, 239, 59, 54),
      ),
      home: const HomeView(),
      routes: {
        '': (context) => const HomeView(),
        '/compose_email': (context) => const EmailInputView(),
      },
    );
  }
}
