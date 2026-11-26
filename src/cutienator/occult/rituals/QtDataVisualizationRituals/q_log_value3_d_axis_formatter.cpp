//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qlogvalue3daxisformatter.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDataVisualization/qlogvalue3daxisformatter.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLogValue3DAxisFormatter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLogValue3DAxisFormatter : QLogValue3DAxisFormatter {
  using QLogValue3DAxisFormatter::createNewInstance;
  using QLogValue3DAxisFormatter::recalculate;
  using QLogValue3DAxisFormatter::positionAt;
  using QLogValue3DAxisFormatter::valueAt;
};

//  A QLogValue3DAxisFormatter that Python can take functions over in. Every QLogValue3DAxisFormatter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLogValue3DAxisFormatterCall0)(const void *, int *);
typedef void (*CuteQLogValue3DAxisFormatterCall1)(const void *, int *);
typedef float (*CuteQLogValue3DAxisFormatterCall2)(const void *, float, int *);
typedef float (*CuteQLogValue3DAxisFormatterCall3)(const void *, float, int *);
typedef QString * (*CuteQLogValue3DAxisFormatterCall4)(const void *, qreal, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLogValue3DAxisFormatterCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLogValue3DAxisFormatterCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValue3DAxisFormatterCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLogValue3DAxisFormatter : public QLogValue3DAxisFormatter {
public:
  using QLogValue3DAxisFormatter::QLogValue3DAxisFormatter;
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
    if (!std::strcmp(key, "_ZNK21QValue3DAxisFormatter10positionAtEf")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QValue3DAxisFormatter7valueAtEf")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QValue3DAxisFormatter14stringForValueEdRK7QString")) {
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

  //  QValue3DAxisFormatter *QLogValue3DAxisFormatter::createNewInstance()
  //      const
  QValue3DAxisFormatter *createNewInstance() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterCall0 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QValue3DAxisFormatter *>(given);
    }
    return QLogValue3DAxisFormatter::createNewInstance();
  }

  //  void QLogValue3DAxisFormatter::recalculate()
  void recalculate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterCall1 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QLogValue3DAxisFormatter::recalculate();
  }

  //  float QLogValue3DAxisFormatter::positionAt(float value) const
  float positionAt(float value) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterCall2 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall2>(taken[2]);
      float given = call(this, value, &handled);
      if (handled) return given;
    }
    return QLogValue3DAxisFormatter::positionAt(value);
  }

  //  float QLogValue3DAxisFormatter::valueAt(float position) const
  float valueAt(float position) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterCall3 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall3>(taken[3]);
      float given = call(this, position, &handled);
      if (handled) return given;
    }
    return QLogValue3DAxisFormatter::valueAt(position);
  }

  //  QString QValue3DAxisFormatter::stringForValue(qreal value, const
  //      QString &format) const
  QString stringForValue(qreal value, const QString &format) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterCall4 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall4>(taken[4]);
      QString * given = call(this, value, &format, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QValue3DAxisFormatter::stringForValue(value, format);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLogValue3DAxisFormatterCall5 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall5>(taken[5]);
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
      CuteQLogValue3DAxisFormatterCall6 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall6>(taken[6]);
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
      CuteQLogValue3DAxisFormatterCall7 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall7>(taken[7]);
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
      CuteQLogValue3DAxisFormatterCall8 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall8>(taken[8]);
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
      CuteQLogValue3DAxisFormatterCall9 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall9>(taken[9]);
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
      CuteQLogValue3DAxisFormatterCall10 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall10>(taken[10]);
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
      CuteQLogValue3DAxisFormatterCall11 call = reinterpret_cast<CuteQLogValue3DAxisFormatterCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLogValue3DAxisFormatter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QLogValue3DAxisFormatter10metaObjectEv(
    const QLogValue3DAxisFormatter *self) {
  return self->metaObject();
}

//  void *QLogValue3DAxisFormatter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QLogValue3DAxisFormatter11qt_metacastEPKc(
    QLogValue3DAxisFormatter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLogValue3DAxisFormatter::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QLogValue3DAxisFormatter11qt_metacallEN11QMetaObject4CallEiPPv(
    QLogValue3DAxisFormatter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLogValue3DAxisFormatter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QLogValue3DAxisFormatter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLogValue3DAxisFormatter::tr(s, c, n));
}

//  QLogValue3DAxisFormatter::QLogValue3DAxisFormatter(QLogValue3DAxisFormatt
//      erPrivate *d, QObject *parent)
extern "C" Q_DECL_EXPORT
QLogValue3DAxisFormatter *ritual_ZN24QLogValue3DAxisFormatterC1EP31QLogValue3DAxisFormatterPrivateP7QObject(
    QLogValue3DAxisFormatterPrivate *d,
    QObject *parent) {
  return new CuteQLogValue3DAxisFormatter(d, parent);
}

//  QLogValue3DAxisFormatter::QLogValue3DAxisFormatter(QObject *parent)
extern "C" Q_DECL_EXPORT
QLogValue3DAxisFormatter *ritual_ZN24QLogValue3DAxisFormatterC1EP7QObject(
    QObject *parent) {
  return new CuteQLogValue3DAxisFormatter(parent);
}

//  QLogValue3DAxisFormatter::~QLogValue3DAxisFormatter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLogValue3DAxisFormatterD1Ev(
    QLogValue3DAxisFormatter *self) {
  delete self;
}

//  void QLogValue3DAxisFormatter::setBase(qreal base)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLogValue3DAxisFormatter7setBaseEd(
    QLogValue3DAxisFormatter *self,
    qreal base) {
  self->setBase(base);
}

//  qreal QLogValue3DAxisFormatter::base() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QLogValue3DAxisFormatter4baseEv(
    const QLogValue3DAxisFormatter *self) {
  return self->base();
}

//  void QLogValue3DAxisFormatter::setAutoSubGrid(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLogValue3DAxisFormatter14setAutoSubGridEb(
    QLogValue3DAxisFormatter *self,
    bool enabled) {
  self->setAutoSubGrid(enabled);
}

//  bool QLogValue3DAxisFormatter::autoSubGrid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QLogValue3DAxisFormatter11autoSubGridEv(
    const QLogValue3DAxisFormatter *self) {
  return self->autoSubGrid();
}

//  void QLogValue3DAxisFormatter::setShowEdgeLabels(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLogValue3DAxisFormatter17setShowEdgeLabelsEb(
    QLogValue3DAxisFormatter *self,
    bool enabled) {
  self->setShowEdgeLabels(enabled);
}

//  bool QLogValue3DAxisFormatter::showEdgeLabels() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QLogValue3DAxisFormatter14showEdgeLabelsEv(
    const QLogValue3DAxisFormatter *self) {
  return self->showEdgeLabels();
}

//  void QLogValue3DAxisFormatter::baseChanged(qreal base)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLogValue3DAxisFormatter11baseChangedEd(
    QLogValue3DAxisFormatter *self,
    qreal base) {
  self->baseChanged(base);
}

//  void QLogValue3DAxisFormatter::autoSubGridChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLogValue3DAxisFormatter18autoSubGridChangedEb(
    QLogValue3DAxisFormatter *self,
    bool enabled) {
  self->autoSubGridChanged(enabled);
}

//  void QLogValue3DAxisFormatter::showEdgeLabelsChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLogValue3DAxisFormatter21showEdgeLabelsChangedEb(
    QLogValue3DAxisFormatter *self,
    bool enabled) {
  self->showEdgeLabelsChanged(enabled);
}

//  QValue3DAxisFormatter *QLogValue3DAxisFormatter::createNewInstance()
//      const
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_ZNK24QLogValue3DAxisFormatter17createNewInstanceEv(
    const QLogValue3DAxisFormatter *self) {
  return self->createNewInstance();
}

//  void QLogValue3DAxisFormatter::recalculate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLogValue3DAxisFormatter11recalculateEv(
    QLogValue3DAxisFormatter *self) {
  self->recalculate();
}

//  float QLogValue3DAxisFormatter::positionAt(float value) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QLogValue3DAxisFormatter10positionAtEf(
    const QLogValue3DAxisFormatter *self,
    float value) {
  return self->positionAt(value);
}

//  float QLogValue3DAxisFormatter::valueAt(float position) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QLogValue3DAxisFormatter7valueAtEf(
    const QLogValue3DAxisFormatter *self,
    float position) {
  return self->valueAt(position);
}

//  void QLogValue3DAxisFormatter::populateCopy(QValue3DAxisFormatter &copy)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QLogValue3DAxisFormatter12populateCopyER21QValue3DAxisFormatter(
    const QLogValue3DAxisFormatter *self,
    QValue3DAxisFormatter *copy) {
  self->populateCopy(*copy);
}

//  QLogValue3DAxisFormatterPrivate *QLogValue3DAxisFormatter::dptr()
extern "C" Q_DECL_EXPORT
QLogValue3DAxisFormatterPrivate *ritual_ZN24QLogValue3DAxisFormatter4dptrEv(
    QLogValue3DAxisFormatter *self) {
  return self->dptr();
}

//  const QLogValue3DAxisFormatterPrivate *QLogValue3DAxisFormatter::dptrc()
//      const
extern "C" Q_DECL_EXPORT
const QLogValue3DAxisFormatterPrivate *ritual_ZNK24QLogValue3DAxisFormatter5dptrcEv(
    const QLogValue3DAxisFormatter *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQLogValue3DAxisFormatter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLogValue3DAxisFormatter(
    QLogValue3DAxisFormatter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLogValue3DAxisFormatter *>(self)->take(key, call);
}

//  QValue3DAxisFormatter *QLogValue3DAxisFormatter::createNewInstance()
//      const
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_own_ZNK24QLogValue3DAxisFormatter17createNewInstanceEv(
    const QLogValue3DAxisFormatter *self) {
  return static_cast<const OwnQLogValue3DAxisFormatter *>(self)->OwnQLogValue3DAxisFormatter::createNewInstance();
}

//  void QLogValue3DAxisFormatter::recalculate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QLogValue3DAxisFormatter11recalculateEv(
    QLogValue3DAxisFormatter *self) {
  static_cast<OwnQLogValue3DAxisFormatter *>(self)->OwnQLogValue3DAxisFormatter::recalculate();
}

//  float QLogValue3DAxisFormatter::positionAt(float value) const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK24QLogValue3DAxisFormatter10positionAtEf(
    const QLogValue3DAxisFormatter *self,
    float value) {
  return static_cast<const OwnQLogValue3DAxisFormatter *>(self)->OwnQLogValue3DAxisFormatter::positionAt(
      value);
}

//  float QLogValue3DAxisFormatter::valueAt(float position) const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK24QLogValue3DAxisFormatter7valueAtEf(
    const QLogValue3DAxisFormatter *self,
    float position) {
  return static_cast<const OwnQLogValue3DAxisFormatter *>(self)->OwnQLogValue3DAxisFormatter::valueAt(
      position);
}
