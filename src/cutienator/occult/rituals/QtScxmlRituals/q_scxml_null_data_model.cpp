//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlnulldatamodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlnulldatamodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtScxml/qscxmlevent.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QScxmlNullDataModel that Python can take functions over in. Every QScxmlNullDataModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQScxmlNullDataModelCall0)(const void *, const QScxmlEvent *, int *);
typedef const QVariant * (*CuteQScxmlNullDataModelCall1)(const void *, const QString *, int *);
typedef bool (*CuteQScxmlNullDataModelCall2)(const void *, const QString *, int *);
typedef bool (*CuteQScxmlNullDataModelCall3)(const void *, const QString *, const QVariant *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlNullDataModelCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlNullDataModelCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlNullDataModelCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlNullDataModelCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlNullDataModelCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlNullDataModelCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlNullDataModelCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlNullDataModel : public QScxmlNullDataModel {
public:
  using QScxmlNullDataModel::QScxmlNullDataModel;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QScxmlDataModel13setScxmlEventERK11QScxmlEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlDataModel13scxmlPropertyERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QScxmlDataModel16hasScxmlPropertyERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QScxmlDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QScxmlNullDataModel::setScxmlEvent(const QScxmlEvent &event)
  void setScxmlEvent(const QScxmlEvent &event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall0 call = reinterpret_cast<CuteQScxmlNullDataModelCall0>(taken[0]);
      call(this, &event, &handled);
      if (handled) return;
    }
    QScxmlNullDataModel::setScxmlEvent(event);
  }

  //  QVariant QScxmlNullDataModel::scxmlProperty(const QString &name)
  //      const
  QVariant scxmlProperty(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall1 call = reinterpret_cast<CuteQScxmlNullDataModelCall1>(taken[1]);
      const QVariant * given = call(this, &name, &handled);
      if (handled && given) return *given;
    }
    return QScxmlNullDataModel::scxmlProperty(name);
  }

  //  bool QScxmlNullDataModel::hasScxmlProperty(const QString &name) const
  bool hasScxmlProperty(const QString &name) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall2 call = reinterpret_cast<CuteQScxmlNullDataModelCall2>(taken[2]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QScxmlNullDataModel::hasScxmlProperty(name);
  }

  //  bool QScxmlNullDataModel::setScxmlProperty(const QString &name, const
  //      QVariant &value, const QString &context)
  bool setScxmlProperty(
      const QString &name,
      const QVariant &value,
      const QString &context) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall3 call = reinterpret_cast<CuteQScxmlNullDataModelCall3>(taken[3]);
      bool given = call(this, &name, &value, &context, &handled);
      if (handled) return given;
    }
    return QScxmlNullDataModel::setScxmlProperty(name, value, context);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall4 call = reinterpret_cast<CuteQScxmlNullDataModelCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall5 call = reinterpret_cast<CuteQScxmlNullDataModelCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall6 call = reinterpret_cast<CuteQScxmlNullDataModelCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall7 call = reinterpret_cast<CuteQScxmlNullDataModelCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall8 call = reinterpret_cast<CuteQScxmlNullDataModelCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall9 call = reinterpret_cast<CuteQScxmlNullDataModelCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQScxmlNullDataModelCall10 call = reinterpret_cast<CuteQScxmlNullDataModelCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlNullDataModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QScxmlNullDataModel10metaObjectEv(
    const QScxmlNullDataModel *self) {
  return self->metaObject();
}

//  void *QScxmlNullDataModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QScxmlNullDataModel11qt_metacastEPKc(
    QScxmlNullDataModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlNullDataModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QScxmlNullDataModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlNullDataModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScxmlNullDataModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QScxmlNullDataModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlNullDataModel::tr(s, c, n));
}

//  QScxmlNullDataModelPrivate *QScxmlNullDataModel::d_func()
extern "C" Q_DECL_EXPORT
QScxmlNullDataModelPrivate *ritual_ZN19QScxmlNullDataModel6d_funcEv(
    QScxmlNullDataModel *self) {
  return self->d_func();
}

//  const QScxmlNullDataModelPrivate *QScxmlNullDataModel::d_func() const
extern "C" Q_DECL_EXPORT
const QScxmlNullDataModelPrivate *ritual_ZNK19QScxmlNullDataModel6d_funcEv(
    const QScxmlNullDataModel *self) {
  return self->d_func();
}

//  QScxmlNullDataModel::QScxmlNullDataModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QScxmlNullDataModel *ritual_ZN19QScxmlNullDataModelC1EP7QObject(
    QObject *parent) {
  return new CuteQScxmlNullDataModel(parent);
}

//  QScxmlNullDataModel::~QScxmlNullDataModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScxmlNullDataModelD1Ev(QScxmlNullDataModel *self) {
  delete self;
}

//  bool QScxmlNullDataModel::setup(const QVariantMap &initialDataValues)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QScxmlNullDataModel5setupERK4QMapI7QString8QVariantE(
    QScxmlNullDataModel *self,
    const QMap<QString, QVariant> *initialDataValues) {
  return self->setup(*initialDataValues);
}

//  QString QScxmlNullDataModel::evaluateToString(QScxmlExecutableContent::Ev
//      aluatorId id, bool *ok)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QScxmlNullDataModel16evaluateToStringEiPb(
    QScxmlNullDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  return new QString(self->evaluateToString(id, ok));
}

//  bool
//      QScxmlNullDataModel::evaluateToBool(QScxmlExecutableContent::Evaluato
//      rId id, bool *ok)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QScxmlNullDataModel14evaluateToBoolEiPb(
    QScxmlNullDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  return self->evaluateToBool(id, ok);
}

//  QVariant QScxmlNullDataModel::evaluateToVariant(QScxmlExecutableContent::
//      EvaluatorId id, bool *ok)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN19QScxmlNullDataModel17evaluateToVariantEiPb(
    QScxmlNullDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  return new QVariant(self->evaluateToVariant(id, ok));
}

//  void
//      QScxmlNullDataModel::evaluateToVoid(QScxmlExecutableContent::Evaluato
//      rId id, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScxmlNullDataModel14evaluateToVoidEiPb(
    QScxmlNullDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  self->evaluateToVoid(id, ok);
}

//  void QScxmlNullDataModel::evaluateAssignment(QScxmlExecutableContent::Eva
//      luatorId id, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScxmlNullDataModel18evaluateAssignmentEiPb(
    QScxmlNullDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  self->evaluateAssignment(id, ok);
}

//  void QScxmlNullDataModel::evaluateInitialization(QScxmlExecutableContent:
//      :EvaluatorId id, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScxmlNullDataModel22evaluateInitializationEiPb(
    QScxmlNullDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok) {
  self->evaluateInitialization(id, ok);
}

//  void
//      QScxmlNullDataModel::evaluateForeach(QScxmlExecutableContent::Evaluat
//      orId id, bool *ok, ForeachLoopBody *body)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScxmlNullDataModel15evaluateForeachEiPbPN15QScxmlDataModel15ForeachLoopBodyE(
    QScxmlNullDataModel *self,
    QScxmlExecutableContent::EvaluatorId id,
    bool *ok,
    QScxmlDataModel::ForeachLoopBody *body) {
  self->evaluateForeach(id, ok, body);
}

//  void QScxmlNullDataModel::setScxmlEvent(const QScxmlEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScxmlNullDataModel13setScxmlEventERK11QScxmlEvent(
    QScxmlNullDataModel *self,
    const QScxmlEvent *event) {
  self->setScxmlEvent(*event);
}

//  QVariant QScxmlNullDataModel::scxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QScxmlNullDataModel13scxmlPropertyERK7QString(
    const QScxmlNullDataModel *self,
    const QString *name) {
  return new QVariant(self->scxmlProperty(*name));
}

//  bool QScxmlNullDataModel::hasScxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QScxmlNullDataModel16hasScxmlPropertyERK7QString(
    const QScxmlNullDataModel *self,
    const QString *name) {
  return self->hasScxmlProperty(*name);
}

//  bool QScxmlNullDataModel::setScxmlProperty(const QString &name, const
//      QVariant &value, const QString &context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QScxmlNullDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_(
    QScxmlNullDataModel *self,
    const QString *name,
    const QVariant *value,
    const QString *context) {
  return self->setScxmlProperty(*name, *value, *context);
}

//  a Python function taken by a CuteQScxmlNullDataModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlNullDataModel(
    QScxmlNullDataModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlNullDataModel *>(self)->take(key, call);
}

//  void QScxmlNullDataModel::setScxmlEvent(const QScxmlEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QScxmlNullDataModel13setScxmlEventERK11QScxmlEvent(
    QScxmlNullDataModel *self,
    const QScxmlEvent *event) {
  self->QScxmlNullDataModel::setScxmlEvent(*event);
}

//  QVariant QScxmlNullDataModel::scxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QScxmlNullDataModel13scxmlPropertyERK7QString(
    const QScxmlNullDataModel *self,
    const QString *name) {
  return new QVariant(self->QScxmlNullDataModel::scxmlProperty(*name));
}

//  bool QScxmlNullDataModel::hasScxmlProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QScxmlNullDataModel16hasScxmlPropertyERK7QString(
    const QScxmlNullDataModel *self,
    const QString *name) {
  return self->QScxmlNullDataModel::hasScxmlProperty(*name);
}

//  bool QScxmlNullDataModel::setScxmlProperty(const QString &name, const
//      QVariant &value, const QString &context)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QScxmlNullDataModel16setScxmlPropertyERK7QStringRK8QVariantS2_(
    QScxmlNullDataModel *self,
    const QString *name,
    const QVariant *value,
    const QString *context) {
  return self->QScxmlNullDataModel::setScxmlProperty(
      *name,
      *value,
      *context);
}
