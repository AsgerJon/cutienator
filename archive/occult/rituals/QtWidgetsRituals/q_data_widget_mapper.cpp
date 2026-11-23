//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdatawidgetmapper.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdatawidgetmapper.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDataWidgetMapper that Python can take functions over in. Every QDataWidgetMapper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDataWidgetMapperCall0)(const void *, int, int *);
typedef bool (*CuteQDataWidgetMapperCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQDataWidgetMapperCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQDataWidgetMapperCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQDataWidgetMapperCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQDataWidgetMapperCall5)(const void *, QEvent *, int *);
typedef void (*CuteQDataWidgetMapperCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQDataWidgetMapperCall7)(const void *, const QMetaMethod *, int *);
class CuteQDataWidgetMapper : public QDataWidgetMapper {
public:
  using QDataWidgetMapper::QDataWidgetMapper;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QDataWidgetMapper15setCurrentIndexEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void QDataWidgetMapper::setCurrentIndex(int index)
  void setCurrentIndex(int index) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDataWidgetMapperCall0 call = reinterpret_cast<CuteQDataWidgetMapperCall0>(taken[0]);
      call(this, index, &handled);
      if (handled) return;
    }
    QDataWidgetMapper::setCurrentIndex(index);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDataWidgetMapperCall1 call = reinterpret_cast<CuteQDataWidgetMapperCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDataWidgetMapperCall2 call = reinterpret_cast<CuteQDataWidgetMapperCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDataWidgetMapperCall3 call = reinterpret_cast<CuteQDataWidgetMapperCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDataWidgetMapperCall4 call = reinterpret_cast<CuteQDataWidgetMapperCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDataWidgetMapperCall5 call = reinterpret_cast<CuteQDataWidgetMapperCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDataWidgetMapperCall6 call = reinterpret_cast<CuteQDataWidgetMapperCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDataWidgetMapperCall7 call = reinterpret_cast<CuteQDataWidgetMapperCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QDataWidgetMapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QDataWidgetMapper10metaObjectEv(
    const QDataWidgetMapper *self) {
  return self->metaObject();
}

//  QString QDataWidgetMapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QDataWidgetMapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDataWidgetMapper::tr(s, c, n));
}

//  QDataWidgetMapper::QDataWidgetMapper(QObject *parent)
extern "C" Q_DECL_EXPORT
QDataWidgetMapper *ritual_ZN17QDataWidgetMapperC1EP7QObject(
    QObject *parent) {
  return new CuteQDataWidgetMapper(parent);
}

//  QDataWidgetMapper::~QDataWidgetMapper()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapperD1Ev(QDataWidgetMapper *self) {
  delete self;
}

//  void QDataWidgetMapper::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper8setModelEP18QAbstractItemModel(
    QDataWidgetMapper *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QAbstractItemModel *QDataWidgetMapper::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK17QDataWidgetMapper5modelEv(
    const QDataWidgetMapper *self) {
  return self->model();
}

//  void QDataWidgetMapper::setItemDelegate(QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper15setItemDelegateEP21QAbstractItemDelegate(
    QDataWidgetMapper *self,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegate(delegate);
}

//  QAbstractItemDelegate *QDataWidgetMapper::itemDelegate() const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QDataWidgetMapper12itemDelegateEv(
    const QDataWidgetMapper *self) {
  return self->itemDelegate();
}

//  void QDataWidgetMapper::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper12setRootIndexERK11QModelIndex(
    QDataWidgetMapper *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  QModelIndex QDataWidgetMapper::rootIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK17QDataWidgetMapper9rootIndexEv(
    const QDataWidgetMapper *self) {
  return new QModelIndex(self->rootIndex());
}

//  void QDataWidgetMapper::setOrientation(Qt::Orientation aOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper14setOrientationEN2Qt11OrientationE(
    QDataWidgetMapper *self,
    Qt::Orientation aOrientation) {
  self->setOrientation(aOrientation);
}

//  Qt::Orientation QDataWidgetMapper::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK17QDataWidgetMapper11orientationEv(
    const QDataWidgetMapper *self) {
  return self->orientation();
}

//  void QDataWidgetMapper::setSubmitPolicy(SubmitPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper15setSubmitPolicyENS_12SubmitPolicyE(
    QDataWidgetMapper *self,
    QDataWidgetMapper::SubmitPolicy policy) {
  self->setSubmitPolicy(policy);
}

//  SubmitPolicy QDataWidgetMapper::submitPolicy() const
extern "C" Q_DECL_EXPORT
QDataWidgetMapper::SubmitPolicy ritual_ZNK17QDataWidgetMapper12submitPolicyEv(
    const QDataWidgetMapper *self) {
  return self->submitPolicy();
}

//  void QDataWidgetMapper::addMapping(QWidget *widget, int section)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper10addMappingEP7QWidgeti(
    QDataWidgetMapper *self,
    QWidget *widget,
    int section) {
  self->addMapping(widget, section);
}

//  void QDataWidgetMapper::addMapping(QWidget *widget, int section, const
//      QByteArray &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper10addMappingEP7QWidgetiRK10QByteArray(
    QDataWidgetMapper *self,
    QWidget *widget,
    int section,
    const QByteArray *propertyName) {
  self->addMapping(widget, section, *propertyName);
}

//  void QDataWidgetMapper::removeMapping(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper13removeMappingEP7QWidget(
    QDataWidgetMapper *self,
    QWidget *widget) {
  self->removeMapping(widget);
}

//  int QDataWidgetMapper::mappedSection(QWidget *widget) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QDataWidgetMapper13mappedSectionEP7QWidget(
    const QDataWidgetMapper *self,
    QWidget *widget) {
  return self->mappedSection(widget);
}

//  QByteArray QDataWidgetMapper::mappedPropertyName(QWidget *widget) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QDataWidgetMapper18mappedPropertyNameEP7QWidget(
    const QDataWidgetMapper *self,
    QWidget *widget) {
  return new QByteArray(self->mappedPropertyName(widget));
}

//  QWidget *QDataWidgetMapper::mappedWidgetAt(int section) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK17QDataWidgetMapper14mappedWidgetAtEi(
    const QDataWidgetMapper *self,
    int section) {
  return self->mappedWidgetAt(section);
}

//  void QDataWidgetMapper::clearMapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper12clearMappingEv(QDataWidgetMapper *self) {
  self->clearMapping();
}

//  int QDataWidgetMapper::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QDataWidgetMapper12currentIndexEv(
    const QDataWidgetMapper *self) {
  return self->currentIndex();
}

//  void QDataWidgetMapper::revert()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper6revertEv(QDataWidgetMapper *self) {
  self->revert();
}

//  bool QDataWidgetMapper::submit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QDataWidgetMapper6submitEv(QDataWidgetMapper *self) {
  return self->submit();
}

//  void QDataWidgetMapper::toFirst()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper7toFirstEv(QDataWidgetMapper *self) {
  self->toFirst();
}

//  void QDataWidgetMapper::toLast()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper6toLastEv(QDataWidgetMapper *self) {
  self->toLast();
}

//  void QDataWidgetMapper::toNext()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper6toNextEv(QDataWidgetMapper *self) {
  self->toNext();
}

//  void QDataWidgetMapper::toPrevious()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper10toPreviousEv(QDataWidgetMapper *self) {
  self->toPrevious();
}

//  void QDataWidgetMapper::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper15setCurrentIndexEi(
    QDataWidgetMapper *self,
    int index) {
  self->setCurrentIndex(index);
}

//  void QDataWidgetMapper::setCurrentModelIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDataWidgetMapper20setCurrentModelIndexERK11QModelIndex(
    QDataWidgetMapper *self,
    const QModelIndex *index) {
  self->setCurrentModelIndex(*index);
}

//  a Python function taken by a CuteQDataWidgetMapper, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDataWidgetMapper(
    QDataWidgetMapper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDataWidgetMapper *>(self)->take(key, call);
}

//  void QDataWidgetMapper::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDataWidgetMapper15setCurrentIndexEi(
    QDataWidgetMapper *self,
    int index) {
  self->QDataWidgetMapper::setCurrentIndex(index);
}
