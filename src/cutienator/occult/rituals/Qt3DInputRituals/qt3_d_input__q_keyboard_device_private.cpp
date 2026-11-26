//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qkeyboarddevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qkeyboarddevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/qkeyboarddevice.h>
#include <Qt3DInput/private/qkeyboarddevice_p.h>
#include <Qt3DInput/qkeyboardhandler.h>
#include <Qt3DCore/private/qscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/frontend/qkeyboarddevice.cpp, line 15, as _ZN9Qt3DInput22QKeyboardDevicePrivateC1Ev
namespace Qt3DInput {
inline QKeyboardDevicePrivate::QKeyboardDevicePrivate()
    : QAbstractPhysicalDevicePrivate()
    , m_activeInput(nullptr)
{
    m_keyMap[QStringLiteral("escape")] = Qt::Key_Escape;
    m_keyMap[QStringLiteral("tab")] = Qt::Key_Tab;
    m_keyMap[QStringLiteral("backtab")] = Qt::Key_Backtab;
    m_keyMap[QStringLiteral("backspace")] = Qt::Key_Backspace;
    m_keyMap[QStringLiteral("return")] = Qt::Key_Return;
    m_keyMap[QStringLiteral("enter")] = Qt::Key_Enter;
    m_keyMap[QStringLiteral("insert")] = Qt::Key_Insert;
    m_keyMap[QStringLiteral("delete")] = Qt::Key_Delete;
    m_keyMap[QStringLiteral("pause")] = Qt::Key_Pause;
    m_keyMap[QStringLiteral("print")] = Qt::Key_Print;
    m_keyMap[QStringLiteral("sysreq")] = Qt::Key_SysReq;
    m_keyMap[QStringLiteral("clear")] = Qt::Key_Clear;
    m_keyMap[QStringLiteral("home")] = Qt::Key_Home;
    m_keyMap[QStringLiteral("end")] = Qt::Key_End;
    m_keyMap[QStringLiteral("left")] = Qt::Key_Left;
    m_keyMap[QStringLiteral("right")] = Qt::Key_Right;
    m_keyMap[QStringLiteral("up")] = Qt::Key_Up;
    m_keyMap[QStringLiteral("down")] = Qt::Key_Down;
    m_keyMap[QStringLiteral("pageUp")] = Qt::Key_PageUp;
    m_keyMap[QStringLiteral("pageDown")] = Qt::Key_PageDown;
    m_keyMap[QStringLiteral("shift")] = Qt::Key_Shift;
    m_keyMap[QStringLiteral("control")] = Qt::Key_Control;
    m_keyMap[QStringLiteral("meta")] = Qt::Key_Meta;
    m_keyMap[QStringLiteral("alt")] = Qt::Key_Alt;
    m_keyMap[QStringLiteral("capLock")] = Qt::Key_CapsLock;
    m_keyMap[QStringLiteral("numLock")] = Qt::Key_NumLock;
    m_keyMap[QStringLiteral("scrollLock")] = Qt::Key_ScrollLock;
    m_keyMap[QStringLiteral("F1")] = Qt::Key_F1;
    m_keyMap[QStringLiteral("F2")] = Qt::Key_F2;
    m_keyMap[QStringLiteral("F3")] = Qt::Key_F3;
    m_keyMap[QStringLiteral("F4")] = Qt::Key_F4;
    m_keyMap[QStringLiteral("F5")] = Qt::Key_F5;
    m_keyMap[QStringLiteral("F6")] = Qt::Key_F6;
    m_keyMap[QStringLiteral("F7")] = Qt::Key_F7;
    m_keyMap[QStringLiteral("F8")] = Qt::Key_F8;
    m_keyMap[QStringLiteral("F9")] = Qt::Key_F9;
    m_keyMap[QStringLiteral("F10")] = Qt::Key_F10;
    m_keyMap[QStringLiteral("F11")] = Qt::Key_F11;
    m_keyMap[QStringLiteral("F12")] = Qt::Key_F12;
    m_keyMap[QStringLiteral("F13")] = Qt::Key_F13;
    m_keyMap[QStringLiteral("F14")] = Qt::Key_F14;
    m_keyMap[QStringLiteral("F15")] = Qt::Key_F15;
    m_keyMap[QStringLiteral("F16")] = Qt::Key_F16;
    m_keyMap[QStringLiteral("F17")] = Qt::Key_F17;
    m_keyMap[QStringLiteral("F18")] = Qt::Key_F18;
    m_keyMap[QStringLiteral("F19")] = Qt::Key_F19;
    m_keyMap[QStringLiteral("F20")] = Qt::Key_F20;
    m_keyMap[QStringLiteral("F21")] = Qt::Key_F21;
    m_keyMap[QStringLiteral("F22")] = Qt::Key_F22;
    m_keyMap[QStringLiteral("F23")] = Qt::Key_F23;
    m_keyMap[QStringLiteral("F24")] = Qt::Key_F24;
    m_keyMap[QStringLiteral("F25")] = Qt::Key_F25;
    m_keyMap[QStringLiteral("F26")] = Qt::Key_F26;
    m_keyMap[QStringLiteral("F27")] = Qt::Key_F27;
    m_keyMap[QStringLiteral("F28")] = Qt::Key_F28;
    m_keyMap[QStringLiteral("F29")] = Qt::Key_F29;
    m_keyMap[QStringLiteral("F30")] = Qt::Key_F30;
    m_keyMap[QStringLiteral("F31")] = Qt::Key_F31;
    m_keyMap[QStringLiteral("F32")] = Qt::Key_F32;
    m_keyMap[QStringLiteral("F33")] = Qt::Key_F33;
    m_keyMap[QStringLiteral("F34")] = Qt::Key_F34;
    m_keyMap[QStringLiteral("F35")] = Qt::Key_F35;
    m_keyMap[QStringLiteral("superL")] = Qt::Key_Super_L;
    m_keyMap[QStringLiteral("superR")] = Qt::Key_Super_R;
    m_keyMap[QStringLiteral("menu")] = Qt::Key_Menu;
    m_keyMap[QStringLiteral("hyperL")] = Qt::Key_Hyper_L;
    m_keyMap[QStringLiteral("hyperR")] = Qt::Key_Hyper_R;
    m_keyMap[QStringLiteral("help")] = Qt::Key_Help;
    m_keyMap[QStringLiteral("directionL")] = Qt::Key_Direction_L;
    m_keyMap[QStringLiteral("directionR")] = Qt::Key_Direction_R;
    m_keyMap[QStringLiteral("space")] = Qt::Key_Space;
    m_keyMap[QStringLiteral("any")] = Qt::Key_Any;
    m_keyMap[QStringLiteral("exclam")] = Qt::Key_Exclam;
    m_keyMap[QStringLiteral("quoteDbl")] = Qt::Key_QuoteDbl;
    m_keyMap[QStringLiteral("numberSign")] = Qt::Key_NumberSign;
    m_keyMap[QStringLiteral("dollar")] = Qt::Key_Dollar;
    m_keyMap[QStringLiteral("percent")] = Qt::Key_Percent;
    m_keyMap[QStringLiteral("ampersand")] = Qt::Key_Ampersand;
    m_keyMap[QStringLiteral("apostrophe")] = Qt::Key_Apostrophe;
    m_keyMap[QStringLiteral("parenLeft")] = Qt::Key_ParenLeft;
    m_keyMap[QStringLiteral("parenRight")] = Qt::Key_ParenRight;
    m_keyMap[QStringLiteral("asterisk")] = Qt::Key_Asterisk;
    m_keyMap[QStringLiteral("plus")] = Qt::Key_Plus;
    m_keyMap[QStringLiteral("comma")] = Qt::Key_Comma;
    m_keyMap[QStringLiteral("minus")] = Qt::Key_Minus;
    m_keyMap[QStringLiteral("period")] = Qt::Key_Period;
    m_keyMap[QStringLiteral("slash")] = Qt::Key_Slash;
    m_keyMap[QStringLiteral("0")] = Qt::Key_0;
    m_keyMap[QStringLiteral("1")] = Qt::Key_1;
    m_keyMap[QStringLiteral("2")] = Qt::Key_2;
    m_keyMap[QStringLiteral("3")] = Qt::Key_3;
    m_keyMap[QStringLiteral("4")] = Qt::Key_4;
    m_keyMap[QStringLiteral("5")] = Qt::Key_5;
    m_keyMap[QStringLiteral("6")] = Qt::Key_6;
    m_keyMap[QStringLiteral("7")] = Qt::Key_7;
    m_keyMap[QStringLiteral("8")] = Qt::Key_8;
    m_keyMap[QStringLiteral("9")] = Qt::Key_9;
    m_keyMap[QStringLiteral("colon")] = Qt::Key_Colon;
    m_keyMap[QStringLiteral("semiColon")] = Qt::Key_Semicolon;
    m_keyMap[QStringLiteral("less")] = Qt::Key_Less;
    m_keyMap[QStringLiteral("equal")] = Qt::Key_Equal;
    m_keyMap[QStringLiteral("greater")] = Qt::Key_Greater;
    m_keyMap[QStringLiteral("question")] = Qt::Key_Question;
    m_keyMap[QStringLiteral("at")] = Qt::Key_At;
    m_keyMap[QStringLiteral("a")] = Qt::Key_A;
    m_keyMap[QStringLiteral("b")] = Qt::Key_B;
    m_keyMap[QStringLiteral("c")] = Qt::Key_C;
    m_keyMap[QStringLiteral("d")] = Qt::Key_D;
    m_keyMap[QStringLiteral("e")] = Qt::Key_E;
    m_keyMap[QStringLiteral("f")] = Qt::Key_F;
    m_keyMap[QStringLiteral("g")] = Qt::Key_G;
    m_keyMap[QStringLiteral("h")] = Qt::Key_H;
    m_keyMap[QStringLiteral("i")] = Qt::Key_I;
    m_keyMap[QStringLiteral("j")] = Qt::Key_J;
    m_keyMap[QStringLiteral("k")] = Qt::Key_K;
    m_keyMap[QStringLiteral("l")] = Qt::Key_L;
    m_keyMap[QStringLiteral("m")] = Qt::Key_M;
    m_keyMap[QStringLiteral("n")] = Qt::Key_N;
    m_keyMap[QStringLiteral("o")] = Qt::Key_O;
    m_keyMap[QStringLiteral("p")] = Qt::Key_P;
    m_keyMap[QStringLiteral("q")] = Qt::Key_Q;
    m_keyMap[QStringLiteral("r")] = Qt::Key_R;
    m_keyMap[QStringLiteral("s")] = Qt::Key_S;
    m_keyMap[QStringLiteral("t")] = Qt::Key_T;
    m_keyMap[QStringLiteral("u")] = Qt::Key_U;
    m_keyMap[QStringLiteral("v")] = Qt::Key_V;
    m_keyMap[QStringLiteral("w")] = Qt::Key_W;
    m_keyMap[QStringLiteral("x")] = Qt::Key_X;
    m_keyMap[QStringLiteral("y")] = Qt::Key_Y;
    m_keyMap[QStringLiteral("z")] = Qt::Key_Z;
    m_keyMap[QStringLiteral("bracketLeft")] = Qt::Key_BracketLeft;
    m_keyMap[QStringLiteral("backslash")] = Qt::Key_Backslash;
    m_keyMap[QStringLiteral("bracketRight")] = Qt::Key_BracketRight;
    m_keyMap[QStringLiteral("asciiCircum")] = Qt::Key_AsciiCircum;
    m_keyMap[QStringLiteral("underscore")] = Qt::Key_Underscore;
    m_keyMap[QStringLiteral("quoteLeft")] = Qt::Key_QuoteLeft;
    m_keyMap[QStringLiteral("braceLeft")] = Qt::Key_BraceLeft;
    m_keyMap[QStringLiteral("bar")] = Qt::Key_Bar;
    m_keyMap[QStringLiteral("braceRight")] = Qt::Key_BraceRight;
    m_keyMap[QStringLiteral("asciiTilde")] = Qt::Key_AsciiTilde;
    m_keyMap[QStringLiteral("plusminus")] = Qt::Key_plusminus;
    m_keyMap[QStringLiteral("onesuperior")] = Qt::Key_onesuperior;
    m_keyMap[QStringLiteral("multiply")] = Qt::Key_multiply;
    m_keyMap[QStringLiteral("division")] = Qt::Key_division;
    m_keyMap[QStringLiteral("diaeresis")] = Qt::Key_diaeresis;

    m_keyNames = m_keyMap.keys();
}
}  // namespace Qt3DInput
//  -----------------------------------------------------------------------

//  A Qt3DInput::QKeyboardDevicePrivate that Python can take functions over in. Every Qt3DInput::QKeyboardDevicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QKeyboardDevicePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QKeyboardDevicePrivateCall1)(const void *, int *);
class CuteQt3DInput_QKeyboardDevicePrivate : public Qt3DInput::QKeyboardDevicePrivate {
public:
  using Qt3DInput::QKeyboardDevicePrivate::QKeyboardDevicePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QKeyboardDevicePrivateCall0 call = reinterpret_cast<CuteQt3DInput_QKeyboardDevicePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QKeyboardDevicePrivateCall1 call = reinterpret_cast<CuteQt3DInput_QKeyboardDevicePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QKeyboardDevicePrivate::QKeyboardDevicePrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardDevicePrivate *ritual_ZN9Qt3DInput22QKeyboardDevicePrivateC1Ev() {
  return new CuteQt3DInput_QKeyboardDevicePrivate();
}

//  QKeyboardDevice *Qt3DInput::QKeyboardDevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardDevice *ritual_ZN9Qt3DInput22QKeyboardDevicePrivate6q_funcEv(
    Qt3DInput::QKeyboardDevicePrivate *self) {
  return self->q_func();
}

//  const QKeyboardDevice *Qt3DInput::QKeyboardDevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QKeyboardDevice *ritual_ZNK9Qt3DInput22QKeyboardDevicePrivate6q_funcEv(
    const Qt3DInput::QKeyboardDevicePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DInput_QKeyboardDevicePrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QKeyboardDevicePrivate(
    Qt3DInput::QKeyboardDevicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QKeyboardDevicePrivate *>(self)->take(key, call);
}
