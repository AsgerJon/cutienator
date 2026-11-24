//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksystempalette_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksystempalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickSystemPalette may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSystemPalette : QQuickSystemPalette {
  using QQuickSystemPalette::eventFilter;
};

//  A QQuickSystemPalette that Python can take functions over in. Every QQuickSystemPalette
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSystemPaletteCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSystemPaletteCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSystemPaletteCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSystemPaletteCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSystemPaletteCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSystemPaletteCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSystemPaletteCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSystemPalette : public QQuickSystemPalette {
public:
  using QQuickSystemPalette::QQuickSystemPalette;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
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
  //  bool QQuickSystemPalette::eventFilter(QObject *watched, QEvent
  //      *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSystemPaletteCall0 call = reinterpret_cast<CuteQQuickSystemPaletteCall0>(taken[0]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QQuickSystemPalette::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSystemPaletteCall1 call = reinterpret_cast<CuteQQuickSystemPaletteCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSystemPaletteCall2 call = reinterpret_cast<CuteQQuickSystemPaletteCall2>(taken[2]);
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
      CuteQQuickSystemPaletteCall3 call = reinterpret_cast<CuteQQuickSystemPaletteCall3>(taken[3]);
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
      CuteQQuickSystemPaletteCall4 call = reinterpret_cast<CuteQQuickSystemPaletteCall4>(taken[4]);
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
      CuteQQuickSystemPaletteCall5 call = reinterpret_cast<CuteQQuickSystemPaletteCall5>(taken[5]);
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
      CuteQQuickSystemPaletteCall6 call = reinterpret_cast<CuteQQuickSystemPaletteCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSystemPalette::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickSystemPalette10metaObjectEv(
    const QQuickSystemPalette *self) {
  return self->metaObject();
}

//  QString QQuickSystemPalette::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickSystemPalette2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSystemPalette::tr(s, c, n));
}

//  QQuickSystemPalette::QQuickSystemPalette(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickSystemPalette *ritual_ZN19QQuickSystemPaletteC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickSystemPalette(parent);
}

//  QColor QQuickSystemPalette::window() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette6windowEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->window());
}

//  QColor QQuickSystemPalette::windowText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette10windowTextEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->windowText());
}

//  QColor QQuickSystemPalette::base() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette4baseEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->base());
}

//  QColor QQuickSystemPalette::text() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette4textEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->text());
}

//  QColor QQuickSystemPalette::alternateBase() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette13alternateBaseEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->alternateBase());
}

//  QColor QQuickSystemPalette::button() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette6buttonEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->button());
}

//  QColor QQuickSystemPalette::buttonText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette10buttonTextEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->buttonText());
}

//  QColor QQuickSystemPalette::light() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette5lightEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->light());
}

//  QColor QQuickSystemPalette::midlight() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette8midlightEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->midlight());
}

//  QColor QQuickSystemPalette::dark() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette4darkEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->dark());
}

//  QColor QQuickSystemPalette::mid() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette3midEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->mid());
}

//  QColor QQuickSystemPalette::shadow() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette6shadowEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->shadow());
}

//  QColor QQuickSystemPalette::highlight() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette9highlightEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->highlight());
}

//  QColor QQuickSystemPalette::highlightedText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette15highlightedTextEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->highlightedText());
}

//  QColor QQuickSystemPalette::placeholderText() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette15placeholderTextEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->placeholderText());
}

//  QColor QQuickSystemPalette::accent() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QQuickSystemPalette6accentEv(
    const QQuickSystemPalette *self) {
  return new QColor(self->accent());
}

//  QQuickSystemPalette::ColorGroup QQuickSystemPalette::colorGroup() const
extern "C" Q_DECL_EXPORT
QQuickSystemPalette::ColorGroup ritual_ZNK19QQuickSystemPalette10colorGroupEv(
    const QQuickSystemPalette *self) {
  return self->colorGroup();
}

//  void QQuickSystemPalette::setColorGroup(QQuickSystemPalette::ColorGroup
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickSystemPalette13setColorGroupENS_10ColorGroupE(
    QQuickSystemPalette *self,
    QQuickSystemPalette::ColorGroup a0) {
  self->setColorGroup(a0);
}

//  bool QQuickSystemPalette::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickSystemPalette11eventFilterEP7QObjectP6QEvent(
    QQuickSystemPalette *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  a Python function taken by a CuteQQuickSystemPalette, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSystemPalette(
    QQuickSystemPalette *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSystemPalette *>(self)->take(key, call);
}

//  bool QQuickSystemPalette::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickSystemPalette11eventFilterEP7QObjectP6QEvent(
    QQuickSystemPalette *self,
    QObject *watched,
    QEvent *event) {
  return static_cast<OwnQQuickSystemPalette *>(self)->OwnQQuickSystemPalette::eventFilter(
      watched,
      event);
}
