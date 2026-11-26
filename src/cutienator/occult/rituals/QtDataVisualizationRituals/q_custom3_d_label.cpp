//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qcustom3dlabel.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qcustom3dlabel.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCustom3DLabel that Python can take functions over in. Every QCustom3DLabel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DLabelCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DLabelCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DLabelCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCustom3DLabel : public QCustom3DLabel {
public:
  using QCustom3DLabel::QCustom3DLabel;
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
      CuteQCustom3DLabelCall0 call = reinterpret_cast<CuteQCustom3DLabelCall0>(taken[0]);
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
      CuteQCustom3DLabelCall1 call = reinterpret_cast<CuteQCustom3DLabelCall1>(taken[1]);
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
      CuteQCustom3DLabelCall2 call = reinterpret_cast<CuteQCustom3DLabelCall2>(taken[2]);
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
      CuteQCustom3DLabelCall3 call = reinterpret_cast<CuteQCustom3DLabelCall3>(taken[3]);
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
      CuteQCustom3DLabelCall4 call = reinterpret_cast<CuteQCustom3DLabelCall4>(taken[4]);
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
      CuteQCustom3DLabelCall5 call = reinterpret_cast<CuteQCustom3DLabelCall5>(taken[5]);
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
      CuteQCustom3DLabelCall6 call = reinterpret_cast<CuteQCustom3DLabelCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCustom3DLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QCustom3DLabel10metaObjectEv(
    const QCustom3DLabel *self) {
  return self->metaObject();
}

//  void *QCustom3DLabel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QCustom3DLabel11qt_metacastEPKc(
    QCustom3DLabel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCustom3DLabel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QCustom3DLabel11qt_metacallEN11QMetaObject4CallEiPPv(
    QCustom3DLabel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCustom3DLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QCustom3DLabel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCustom3DLabel::tr(s, c, n));
}

//  QCustom3DLabel::QCustom3DLabel(QObject *parent)
extern "C" Q_DECL_EXPORT
QCustom3DLabel *ritual_ZN14QCustom3DLabelC1EP7QObject(QObject *parent) {
  return new CuteQCustom3DLabel(parent);
}

//  QCustom3DLabel::QCustom3DLabel(const QString &text, const QFont &font,
//      const QVector3D &position, const QVector3D &scaling, const
//      QQuaternion &rotation, QObject *parent)
extern "C" Q_DECL_EXPORT
QCustom3DLabel *ritual_ZN14QCustom3DLabelC1ERK7QStringRK5QFontRK9QVector3DS8_RK11QQuaternionP7QObject(
    const QString *text,
    const QFont *font,
    const QVector3D *position,
    const QVector3D *scaling,
    const QQuaternion *rotation,
    QObject *parent) {
  return new CuteQCustom3DLabel(
      *text,
      *font,
      *position,
      *scaling,
      *rotation,
      parent);
}

//  QCustom3DLabel::~QCustom3DLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabelD1Ev(QCustom3DLabel *self) {
  delete self;
}

//  void QCustom3DLabel::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel7setTextERK7QString(
    QCustom3DLabel *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QCustom3DLabel::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QCustom3DLabel4textEv(const QCustom3DLabel *self) {
  return new QString(self->text());
}

//  void QCustom3DLabel::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel7setFontERK5QFont(
    QCustom3DLabel *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QFont QCustom3DLabel::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QCustom3DLabel4fontEv(const QCustom3DLabel *self) {
  return new QFont(self->font());
}

//  void QCustom3DLabel::setTextColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel12setTextColorERK6QColor(
    QCustom3DLabel *self,
    const QColor *color) {
  self->setTextColor(*color);
}

//  QColor QCustom3DLabel::textColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QCustom3DLabel9textColorEv(const QCustom3DLabel *self) {
  return new QColor(self->textColor());
}

//  void QCustom3DLabel::setBackgroundColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel18setBackgroundColorERK6QColor(
    QCustom3DLabel *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  QColor QCustom3DLabel::backgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QCustom3DLabel15backgroundColorEv(
    const QCustom3DLabel *self) {
  return new QColor(self->backgroundColor());
}

//  void QCustom3DLabel::setBorderEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel16setBorderEnabledEb(
    QCustom3DLabel *self,
    bool enabled) {
  self->setBorderEnabled(enabled);
}

//  bool QCustom3DLabel::isBorderEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QCustom3DLabel15isBorderEnabledEv(
    const QCustom3DLabel *self) {
  return self->isBorderEnabled();
}

//  void QCustom3DLabel::setBackgroundEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel20setBackgroundEnabledEb(
    QCustom3DLabel *self,
    bool enabled) {
  self->setBackgroundEnabled(enabled);
}

//  bool QCustom3DLabel::isBackgroundEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QCustom3DLabel19isBackgroundEnabledEv(
    const QCustom3DLabel *self) {
  return self->isBackgroundEnabled();
}

//  void QCustom3DLabel::setFacingCamera(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel15setFacingCameraEb(
    QCustom3DLabel *self,
    bool enabled) {
  self->setFacingCamera(enabled);
}

//  bool QCustom3DLabel::isFacingCamera() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QCustom3DLabel14isFacingCameraEv(
    const QCustom3DLabel *self) {
  return self->isFacingCamera();
}

//  void QCustom3DLabel::textChanged(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel11textChangedERK7QString(
    QCustom3DLabel *self,
    const QString *text) {
  self->textChanged(*text);
}

//  void QCustom3DLabel::fontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel11fontChangedERK5QFont(
    QCustom3DLabel *self,
    const QFont *font) {
  self->fontChanged(*font);
}

//  void QCustom3DLabel::textColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel16textColorChangedERK6QColor(
    QCustom3DLabel *self,
    const QColor *color) {
  self->textColorChanged(*color);
}

//  void QCustom3DLabel::backgroundColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel22backgroundColorChangedERK6QColor(
    QCustom3DLabel *self,
    const QColor *color) {
  self->backgroundColorChanged(*color);
}

//  void QCustom3DLabel::borderEnabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel20borderEnabledChangedEb(
    QCustom3DLabel *self,
    bool enabled) {
  self->borderEnabledChanged(enabled);
}

//  void QCustom3DLabel::backgroundEnabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel24backgroundEnabledChangedEb(
    QCustom3DLabel *self,
    bool enabled) {
  self->backgroundEnabledChanged(enabled);
}

//  void QCustom3DLabel::facingCameraChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCustom3DLabel19facingCameraChangedEb(
    QCustom3DLabel *self,
    bool enabled) {
  self->facingCameraChanged(enabled);
}

//  QCustom3DLabelPrivate *QCustom3DLabel::dptr()
extern "C" Q_DECL_EXPORT
QCustom3DLabelPrivate *ritual_ZN14QCustom3DLabel4dptrEv(
    QCustom3DLabel *self) {
  return self->dptr();
}

//  const QCustom3DLabelPrivate *QCustom3DLabel::dptrc() const
extern "C" Q_DECL_EXPORT
const QCustom3DLabelPrivate *ritual_ZNK14QCustom3DLabel5dptrcEv(
    const QCustom3DLabel *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQCustom3DLabel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCustom3DLabel(
    QCustom3DLabel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCustom3DLabel *>(self)->take(key, call);
}
