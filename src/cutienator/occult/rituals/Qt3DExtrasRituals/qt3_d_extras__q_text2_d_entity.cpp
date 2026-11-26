//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qtext2dentity.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qtext2dentity.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QText2DEntity that Python can take functions over in. Every Qt3DExtras::QText2DEntity
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QText2DEntityCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QText2DEntityCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DEntityCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DEntityCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DEntityCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DEntityCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QText2DEntityCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QText2DEntity : public Qt3DExtras::QText2DEntity {
public:
  using Qt3DExtras::QText2DEntity::QText2DEntity;
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
      CuteQt3DExtras_QText2DEntityCall0 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityCall0>(taken[0]);
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
      CuteQt3DExtras_QText2DEntityCall1 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityCall1>(taken[1]);
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
      CuteQt3DExtras_QText2DEntityCall2 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityCall2>(taken[2]);
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
      CuteQt3DExtras_QText2DEntityCall3 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityCall3>(taken[3]);
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
      CuteQt3DExtras_QText2DEntityCall4 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityCall4>(taken[4]);
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
      CuteQt3DExtras_QText2DEntityCall5 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityCall5>(taken[5]);
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
      CuteQt3DExtras_QText2DEntityCall6 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QText2DEntity::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras13QText2DEntity10metaObjectEv(
    const Qt3DExtras::QText2DEntity *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QText2DEntity::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras13QText2DEntity11qt_metacastEPKc(
    Qt3DExtras::QText2DEntity *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QText2DEntity::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras13QText2DEntity11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QText2DEntity *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QText2DEntity::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras13QText2DEntity2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QText2DEntity::tr(s, c, n));
}

//  Qt3DExtras::QText2DEntity::QText2DEntity(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QText2DEntity *ritual_ZN10Qt3DExtras13QText2DEntityC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QText2DEntity(parent);
}

//  Qt3DExtras::QText2DEntity::~QText2DEntity()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntityD1Ev(
    Qt3DExtras::QText2DEntity *self) {
  delete self;
}

//  QFont Qt3DExtras::QText2DEntity::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK10Qt3DExtras13QText2DEntity4fontEv(
    const Qt3DExtras::QText2DEntity *self) {
  return new QFont(self->font());
}

//  void Qt3DExtras::QText2DEntity::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity7setFontERK5QFont(
    Qt3DExtras::QText2DEntity *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QColor Qt3DExtras::QText2DEntity::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras13QText2DEntity5colorEv(
    const Qt3DExtras::QText2DEntity *self) {
  return new QColor(self->color());
}

//  void Qt3DExtras::QText2DEntity::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity8setColorERK6QColor(
    Qt3DExtras::QText2DEntity *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QString Qt3DExtras::QText2DEntity::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DExtras13QText2DEntity4textEv(
    const Qt3DExtras::QText2DEntity *self) {
  return new QString(self->text());
}

//  void Qt3DExtras::QText2DEntity::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity7setTextERK7QString(
    Qt3DExtras::QText2DEntity *self,
    const QString *text) {
  self->setText(*text);
}

//  float Qt3DExtras::QText2DEntity::width() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras13QText2DEntity5widthEv(
    const Qt3DExtras::QText2DEntity *self) {
  return self->width();
}

//  float Qt3DExtras::QText2DEntity::height() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras13QText2DEntity6heightEv(
    const Qt3DExtras::QText2DEntity *self) {
  return self->height();
}

//  void Qt3DExtras::QText2DEntity::setWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity8setWidthEf(
    Qt3DExtras::QText2DEntity *self,
    float width) {
  self->setWidth(width);
}

//  void Qt3DExtras::QText2DEntity::setHeight(float height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity9setHeightEf(
    Qt3DExtras::QText2DEntity *self,
    float height) {
  self->setHeight(height);
}

//  Qt::Alignment Qt3DExtras::QText2DEntity::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DExtras13QText2DEntity9alignmentEv(
    const Qt3DExtras::QText2DEntity *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void Qt3DExtras::QText2DEntity::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    Qt3DExtras::QText2DEntity *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void Qt3DExtras::QText2DEntity::fontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity11fontChangedERK5QFont(
    Qt3DExtras::QText2DEntity *self,
    const QFont *font) {
  self->fontChanged(*font);
}

//  void Qt3DExtras::QText2DEntity::colorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity12colorChangedERK6QColor(
    Qt3DExtras::QText2DEntity *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void Qt3DExtras::QText2DEntity::textChanged(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity11textChangedERK7QString(
    Qt3DExtras::QText2DEntity *self,
    const QString *text) {
  self->textChanged(*text);
}

//  void Qt3DExtras::QText2DEntity::widthChanged(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity12widthChangedEf(
    Qt3DExtras::QText2DEntity *self,
    float width) {
  self->widthChanged(width);
}

//  void Qt3DExtras::QText2DEntity::heightChanged(float height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras13QText2DEntity13heightChangedEf(
    Qt3DExtras::QText2DEntity *self,
    float height) {
  self->heightChanged(height);
}

//  QText2DEntityPrivate *Qt3DExtras::QText2DEntity::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QText2DEntityPrivate *ritual_ZN10Qt3DExtras13QText2DEntity6d_funcEv(
    Qt3DExtras::QText2DEntity *self) {
  return self->d_func();
}

//  const QText2DEntityPrivate *Qt3DExtras::QText2DEntity::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QText2DEntityPrivate *ritual_ZNK10Qt3DExtras13QText2DEntity6d_funcEv(
    const Qt3DExtras::QText2DEntity *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QText2DEntity, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QText2DEntity(
    Qt3DExtras::QText2DEntity *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QText2DEntity *>(self)->take(key, call);
}
