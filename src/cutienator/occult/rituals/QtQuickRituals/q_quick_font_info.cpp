//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickfontinfo_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickfontinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qfontvariableaxis.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickFontInfo that Python can take functions over in. Every QQuickFontInfo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFontInfoCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFontInfoCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontInfoCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontInfoCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontInfoCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontInfoCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontInfoCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickFontInfo : public QQuickFontInfo {
public:
  using QQuickFontInfo::QQuickFontInfo;
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
      CuteQQuickFontInfoCall0 call = reinterpret_cast<CuteQQuickFontInfoCall0>(taken[0]);
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
      CuteQQuickFontInfoCall1 call = reinterpret_cast<CuteQQuickFontInfoCall1>(taken[1]);
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
      CuteQQuickFontInfoCall2 call = reinterpret_cast<CuteQQuickFontInfoCall2>(taken[2]);
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
      CuteQQuickFontInfoCall3 call = reinterpret_cast<CuteQQuickFontInfoCall3>(taken[3]);
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
      CuteQQuickFontInfoCall4 call = reinterpret_cast<CuteQQuickFontInfoCall4>(taken[4]);
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
      CuteQQuickFontInfoCall5 call = reinterpret_cast<CuteQQuickFontInfoCall5>(taken[5]);
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
      CuteQQuickFontInfoCall6 call = reinterpret_cast<CuteQQuickFontInfoCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickFontInfo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickFontInfo10metaObjectEv(
    const QQuickFontInfo *self) {
  return self->metaObject();
}

//  QString QQuickFontInfo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickFontInfo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFontInfo::tr(s, c, n));
}

//  QQuickFontInfo::QQuickFontInfo(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFontInfo *ritual_ZN14QQuickFontInfoC1EP7QObject(QObject *parent) {
  return new CuteQQuickFontInfo(parent);
}

//  QQuickFontInfo::~QQuickFontInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFontInfoD1Ev(QQuickFontInfo *self) {
  delete self;
}

//  QFont QQuickFontInfo::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQuickFontInfo4fontEv(const QQuickFontInfo *self) {
  return new QFont(self->font());
}

//  void QQuickFontInfo::setFont(QFont font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickFontInfo7setFontE5QFont(
    QQuickFontInfo *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QString QQuickFontInfo::family() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickFontInfo6familyEv(const QQuickFontInfo *self) {
  return new QString(self->family());
}

//  QString QQuickFontInfo::styleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickFontInfo9styleNameEv(const QQuickFontInfo *self) {
  return new QString(self->styleName());
}

//  int QQuickFontInfo::pixelSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickFontInfo9pixelSizeEv(const QQuickFontInfo *self) {
  return self->pixelSize();
}

//  qreal QQuickFontInfo::pointSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickFontInfo9pointSizeEv(const QQuickFontInfo *self) {
  return self->pointSize();
}

//  bool QQuickFontInfo::italic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickFontInfo6italicEv(const QQuickFontInfo *self) {
  return self->italic();
}

//  int QQuickFontInfo::weight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickFontInfo6weightEv(const QQuickFontInfo *self) {
  return self->weight();
}

//  bool QQuickFontInfo::bold() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickFontInfo4boldEv(const QQuickFontInfo *self) {
  return self->bold();
}

//  bool QQuickFontInfo::fixedPitch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickFontInfo10fixedPitchEv(const QQuickFontInfo *self) {
  return self->fixedPitch();
}

//  QQuickFontEnums::Style QQuickFontInfo::style() const
extern "C" Q_DECL_EXPORT
QQuickFontEnums::Style ritual_ZNK14QQuickFontInfo5styleEv(
    const QQuickFontInfo *self) {
  return self->style();
}

//  QList<QFontVariableAxis> QQuickFontInfo::variableAxes() const
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_ZNK14QQuickFontInfo12variableAxesEv(
    const QQuickFontInfo *self) {
  return new QList<QFontVariableAxis>(self->variableAxes());
}

//  a Python function taken by a CuteQQuickFontInfo, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFontInfo(
    QQuickFontInfo *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFontInfo *>(self)->take(key, call);
}
