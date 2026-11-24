//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qvalue3daxisformatter.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtDataVisualization/qvalue3daxisformatter.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QValue3DAxisFormatter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQValue3DAxisFormatter : QValue3DAxisFormatter {
  using QValue3DAxisFormatter::createNewInstance;
  using QValue3DAxisFormatter::recalculate;
  using QValue3DAxisFormatter::stringForValue;
  using QValue3DAxisFormatter::positionAt;
  using QValue3DAxisFormatter::valueAt;
};

//  A QValue3DAxisFormatter that Python can take functions over in. Every QValue3DAxisFormatter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQValue3DAxisFormatterCall0)(const void *, int *);
typedef void (*CuteQValue3DAxisFormatterCall1)(const void *, int *);
typedef QString * (*CuteQValue3DAxisFormatterCall2)(const void *, qreal, const QString *, int *);
typedef float (*CuteQValue3DAxisFormatterCall3)(const void *, float, int *);
typedef float (*CuteQValue3DAxisFormatterCall4)(const void *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValue3DAxisFormatterCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValue3DAxisFormatterCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValue3DAxisFormatterCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQValue3DAxisFormatter : public QValue3DAxisFormatter {
public:
  using QValue3DAxisFormatter::QValue3DAxisFormatter;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QValue3DAxisFormatter17createNewInstanceEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QValue3DAxisFormatter11recalculateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QValue3DAxisFormatter14stringForValueEdRK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QValue3DAxisFormatter10positionAtEf")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QValue3DAxisFormatter7valueAtEf")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QValue3DAxisFormatter *QValue3DAxisFormatter::createNewInstance()
  //      const
  QValue3DAxisFormatter *createNewInstance() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall0 call = reinterpret_cast<CuteQValue3DAxisFormatterCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QValue3DAxisFormatter *>(given);
    }
    return QValue3DAxisFormatter::createNewInstance();
  }

  //  void QValue3DAxisFormatter::recalculate()
  void recalculate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall1 call = reinterpret_cast<CuteQValue3DAxisFormatterCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QValue3DAxisFormatter::recalculate();
  }

  //  QString QValue3DAxisFormatter::stringForValue(qreal value, const
  //      QString &format) const
  QString stringForValue(qreal value, const QString &format) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall2 call = reinterpret_cast<CuteQValue3DAxisFormatterCall2>(taken[2]);
      QString * given = call(this, value, &format, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QValue3DAxisFormatter::stringForValue(value, format);
  }

  //  float QValue3DAxisFormatter::positionAt(float value) const
  float positionAt(float value) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall3 call = reinterpret_cast<CuteQValue3DAxisFormatterCall3>(taken[3]);
      float given = call(this, value, &handled);
      if (handled) return given;
    }
    return QValue3DAxisFormatter::positionAt(value);
  }

  //  float QValue3DAxisFormatter::valueAt(float position) const
  float valueAt(float position) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall4 call = reinterpret_cast<CuteQValue3DAxisFormatterCall4>(taken[4]);
      float given = call(this, position, &handled);
      if (handled) return given;
    }
    return QValue3DAxisFormatter::valueAt(position);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall5 call = reinterpret_cast<CuteQValue3DAxisFormatterCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall6 call = reinterpret_cast<CuteQValue3DAxisFormatterCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall7 call = reinterpret_cast<CuteQValue3DAxisFormatterCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall8 call = reinterpret_cast<CuteQValue3DAxisFormatterCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall9 call = reinterpret_cast<CuteQValue3DAxisFormatterCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall10 call = reinterpret_cast<CuteQValue3DAxisFormatterCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQValue3DAxisFormatterCall11 call = reinterpret_cast<CuteQValue3DAxisFormatterCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QValue3DAxisFormatter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QValue3DAxisFormatter10metaObjectEv(
    const QValue3DAxisFormatter *self) {
  return self->metaObject();
}

//  QString QValue3DAxisFormatter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QValue3DAxisFormatter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QValue3DAxisFormatter::tr(s, c, n));
}

//  QValue3DAxisFormatter::QValue3DAxisFormatter(QValue3DAxisFormatterPrivate
//      *d, QObject *parent)
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_ZN21QValue3DAxisFormatterC1EP28QValue3DAxisFormatterPrivateP7QObject(
    QValue3DAxisFormatterPrivate *d,
    QObject *parent) {
  return new CuteQValue3DAxisFormatter(d, parent);
}

//  QValue3DAxisFormatter::QValue3DAxisFormatter(QObject *parent)
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_ZN21QValue3DAxisFormatterC1EP7QObject(
    QObject *parent) {
  return new CuteQValue3DAxisFormatter(parent);
}

//  QValue3DAxisFormatter::~QValue3DAxisFormatter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QValue3DAxisFormatterD1Ev(QValue3DAxisFormatter *self) {
  delete self;
}

//  void QValue3DAxisFormatter::setAllowNegatives(bool allow)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QValue3DAxisFormatter17setAllowNegativesEb(
    QValue3DAxisFormatter *self,
    bool allow) {
  self->setAllowNegatives(allow);
}

//  bool QValue3DAxisFormatter::allowNegatives() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QValue3DAxisFormatter14allowNegativesEv(
    const QValue3DAxisFormatter *self) {
  return self->allowNegatives();
}

//  void QValue3DAxisFormatter::setAllowZero(bool allow)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QValue3DAxisFormatter12setAllowZeroEb(
    QValue3DAxisFormatter *self,
    bool allow) {
  self->setAllowZero(allow);
}

//  bool QValue3DAxisFormatter::allowZero() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QValue3DAxisFormatter9allowZeroEv(
    const QValue3DAxisFormatter *self) {
  return self->allowZero();
}

//  QValue3DAxisFormatter *QValue3DAxisFormatter::createNewInstance() const
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_ZNK21QValue3DAxisFormatter17createNewInstanceEv(
    const QValue3DAxisFormatter *self) {
  return self->createNewInstance();
}

//  void QValue3DAxisFormatter::recalculate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QValue3DAxisFormatter11recalculateEv(
    QValue3DAxisFormatter *self) {
  self->recalculate();
}

//  QString QValue3DAxisFormatter::stringForValue(qreal value, const QString
//      &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QValue3DAxisFormatter14stringForValueEdRK7QString(
    const QValue3DAxisFormatter *self,
    qreal value,
    const QString *format) {
  return new QString(self->stringForValue(value, *format));
}

//  float QValue3DAxisFormatter::positionAt(float value) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QValue3DAxisFormatter10positionAtEf(
    const QValue3DAxisFormatter *self,
    float value) {
  return self->positionAt(value);
}

//  float QValue3DAxisFormatter::valueAt(float position) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK21QValue3DAxisFormatter7valueAtEf(
    const QValue3DAxisFormatter *self,
    float position) {
  return self->valueAt(position);
}

//  void QValue3DAxisFormatter::markDirty(bool labelsChange)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QValue3DAxisFormatter9markDirtyEb(
    QValue3DAxisFormatter *self,
    bool labelsChange) {
  self->markDirty(labelsChange);
}

//  QValue3DAxis *QValue3DAxisFormatter::axis() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK21QValue3DAxisFormatter4axisEv(
    const QValue3DAxisFormatter *self) {
  return self->axis();
}

//  void QValue3DAxisFormatter::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QValue3DAxisFormatter9setLocaleERK7QLocale(
    QValue3DAxisFormatter *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QValue3DAxisFormatter::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK21QValue3DAxisFormatter6localeEv(
    const QValue3DAxisFormatter *self) {
  return new QLocale(self->locale());
}

//  a Python function taken by a CuteQValue3DAxisFormatter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValue3DAxisFormatter(
    QValue3DAxisFormatter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQValue3DAxisFormatter *>(self)->take(key, call);
}

//  QValue3DAxisFormatter *QValue3DAxisFormatter::createNewInstance() const
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_own_ZNK21QValue3DAxisFormatter17createNewInstanceEv(
    const QValue3DAxisFormatter *self) {
  return static_cast<const OwnQValue3DAxisFormatter *>(self)->OwnQValue3DAxisFormatter::createNewInstance();
}

//  void QValue3DAxisFormatter::recalculate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QValue3DAxisFormatter11recalculateEv(
    QValue3DAxisFormatter *self) {
  static_cast<OwnQValue3DAxisFormatter *>(self)->OwnQValue3DAxisFormatter::recalculate();
}

//  QString QValue3DAxisFormatter::stringForValue(qreal value, const QString
//      &format) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QValue3DAxisFormatter14stringForValueEdRK7QString(
    const QValue3DAxisFormatter *self,
    qreal value,
    const QString *format) {
  return new QString(
      static_cast<const OwnQValue3DAxisFormatter *>(self)->OwnQValue3DAxisFormatter::stringForValue(
          value,
          *format));
}

//  float QValue3DAxisFormatter::positionAt(float value) const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK21QValue3DAxisFormatter10positionAtEf(
    const QValue3DAxisFormatter *self,
    float value) {
  return static_cast<const OwnQValue3DAxisFormatter *>(self)->OwnQValue3DAxisFormatter::positionAt(
      value);
}

//  float QValue3DAxisFormatter::valueAt(float position) const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK21QValue3DAxisFormatter7valueAtEf(
    const QValue3DAxisFormatter *self,
    float position) {
  return static_cast<const OwnQValue3DAxisFormatter *>(self)->OwnQValue3DAxisFormatter::valueAt(
      position);
}
