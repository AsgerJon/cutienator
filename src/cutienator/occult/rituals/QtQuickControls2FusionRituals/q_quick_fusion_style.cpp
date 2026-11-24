//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Fusion/6.12.0/QtQuickControls2Fusion/private/qquickfusionstyle_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2Fusion/QtQuickControls2Fusion>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Fusion/6.12.0/QtQuickControls2Fusion/private/qquickfusionstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickFusionStyle that Python can take functions over in. Every QQuickFusionStyle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFusionStyleCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFusionStyleCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFusionStyleCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFusionStyleCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFusionStyleCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFusionStyleCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFusionStyleCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickFusionStyle : public QQuickFusionStyle {
public:
  using QQuickFusionStyle::QQuickFusionStyle;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFusionStyleCall0 call = reinterpret_cast<CuteQQuickFusionStyleCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFusionStyleCall1 call = reinterpret_cast<CuteQQuickFusionStyleCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFusionStyleCall2 call = reinterpret_cast<CuteQQuickFusionStyleCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickFusionStyleCall3 call = reinterpret_cast<CuteQQuickFusionStyleCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickFusionStyleCall4 call = reinterpret_cast<CuteQQuickFusionStyleCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickFusionStyleCall5 call = reinterpret_cast<CuteQQuickFusionStyleCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickFusionStyleCall6 call = reinterpret_cast<CuteQQuickFusionStyleCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickFusionStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickFusionStyle10metaObjectEv(
    const QQuickFusionStyle *self) {
  return self->metaObject();
}

//  QString QQuickFusionStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickFusionStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFusionStyle::tr(s, c, n));
}

//  void QQuickFusionStyle::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickFusionStyle22qt_qmlMarker_singletonEv(
    QQuickFusionStyle *self) {
  self->qt_qmlMarker_singleton();
}

//  QQuickFusionStyle::QQuickFusionStyle(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFusionStyle *ritual_ZN17QQuickFusionStyleC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickFusionStyle(parent);
}

//  QColor QQuickFusionStyle::lightShade()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle10lightShadeEv() {
  return new QColor(QQuickFusionStyle::lightShade());
}

//  QColor QQuickFusionStyle::darkShade()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle9darkShadeEv() {
  return new QColor(QQuickFusionStyle::darkShade());
}

//  QColor QQuickFusionStyle::topShadow()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle9topShadowEv() {
  return new QColor(QQuickFusionStyle::topShadow());
}

//  QColor QQuickFusionStyle::innerContrastLine()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle17innerContrastLineEv() {
  return new QColor(QQuickFusionStyle::innerContrastLine());
}

//  bool QQuickFusionStyle::isHighContrast()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickFusionStyle14isHighContrastEv() {
  return QQuickFusionStyle::isHighContrast();
}

//  QColor QQuickFusionStyle::highlight(QQuickPalette *palette)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle9highlightEP13QQuickPalette(
    QQuickPalette *palette) {
  return new QColor(QQuickFusionStyle::highlight(palette));
}

//  QColor QQuickFusionStyle::highlightedText(QQuickPalette *palette)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle15highlightedTextEP13QQuickPalette(
    QQuickPalette *palette) {
  return new QColor(QQuickFusionStyle::highlightedText(palette));
}

//  QColor QQuickFusionStyle::outline(QQuickPalette *palette)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle7outlineEP13QQuickPalette(
    QQuickPalette *palette) {
  return new QColor(QQuickFusionStyle::outline(palette));
}

//  QColor QQuickFusionStyle::highlightedOutline(QQuickPalette *palette)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle18highlightedOutlineEP13QQuickPalette(
    QQuickPalette *palette) {
  return new QColor(QQuickFusionStyle::highlightedOutline(palette));
}

//  QColor QQuickFusionStyle::tabFrameColor(QQuickPalette *palette)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle13tabFrameColorEP13QQuickPalette(
    QQuickPalette *palette) {
  return new QColor(QQuickFusionStyle::tabFrameColor(palette));
}

//  QColor QQuickFusionStyle::buttonColor(QQuickPalette *palette, bool
//      highlighted, bool down, bool hovered)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle11buttonColorEP13QQuickPalettebbb(
    QQuickPalette *palette,
    bool highlighted,
    bool down,
    bool hovered) {
  return new QColor(
      QQuickFusionStyle::buttonColor(
          palette,
          highlighted,
          down,
          hovered));
}

//  QColor QQuickFusionStyle::buttonOutline(QQuickPalette *palette, bool
//      highlighted, bool enabled)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle13buttonOutlineEP13QQuickPalettebb(
    QQuickPalette *palette,
    bool highlighted,
    bool enabled) {
  return new QColor(
      QQuickFusionStyle::buttonOutline(
          palette,
          highlighted,
          enabled));
}

//  QColor QQuickFusionStyle::gradientStart(const QColor &baseColor)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle13gradientStartERK6QColor(
    const QColor *baseColor) {
  return new QColor(QQuickFusionStyle::gradientStart(*baseColor));
}

//  QColor QQuickFusionStyle::gradientStop(const QColor &baseColor)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle12gradientStopERK6QColor(
    const QColor *baseColor) {
  return new QColor(QQuickFusionStyle::gradientStop(*baseColor));
}

//  QColor QQuickFusionStyle::mergedColors(const QColor &colorA, const QColor
//      &colorB, int factor)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle12mergedColorsERK6QColorS2_i(
    const QColor *colorA,
    const QColor *colorB,
    int factor) {
  return new QColor(
      QQuickFusionStyle::mergedColors(
          *colorA,
          *colorB,
          factor));
}

//  QColor QQuickFusionStyle::grooveColor(QQuickPalette *palette)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN17QQuickFusionStyle11grooveColorEP13QQuickPalette(
    QQuickPalette *palette) {
  return new QColor(QQuickFusionStyle::grooveColor(palette));
}

//  a Python function taken by a CuteQQuickFusionStyle, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFusionStyle(
    QQuickFusionStyle *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFusionStyle *>(self)->take(key, call);
}
