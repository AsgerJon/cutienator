//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/metadatabase_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/metadatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A qdesigner_internal::MetaDataBaseItem that Python can take functions over in. Every qdesigner_internal::MetaDataBaseItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*Cuteqdesigner_internal_MetaDataBaseItemCall0)(const void *, int *);
typedef void (*Cuteqdesigner_internal_MetaDataBaseItemCall1)(const void *, const QString *, int *);
typedef bool (*Cuteqdesigner_internal_MetaDataBaseItemCall2)(const void *, int *);
typedef void (*Cuteqdesigner_internal_MetaDataBaseItemCall3)(const void *, bool, int *);
class Cuteqdesigner_internal_MetaDataBaseItem : public qdesigner_internal::MetaDataBaseItem {
public:
  using qdesigner_internal::MetaDataBaseItem::MetaDataBaseItem;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK34QDesignerMetaDataBaseItemInterface4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerMetaDataBaseItemInterface7setNameERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerMetaDataBaseItemInterface7enabledEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerMetaDataBaseItemInterface10setEnabledEb")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QString qdesigner_internal::MetaDataBaseItem::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseItemCall0 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseItemCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return qdesigner_internal::MetaDataBaseItem::name();
  }

  //  void qdesigner_internal::MetaDataBaseItem::setName(const QString
  //      &name)
  void setName(const QString &name) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseItemCall1 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseItemCall1>(taken[1]);
      call(this, &name, &handled);
      if (handled) return;
    }
    qdesigner_internal::MetaDataBaseItem::setName(name);
  }

  //  bool qdesigner_internal::MetaDataBaseItem::enabled() const
  bool enabled() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseItemCall2 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseItemCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return qdesigner_internal::MetaDataBaseItem::enabled();
  }

  //  void qdesigner_internal::MetaDataBaseItem::setEnabled(bool b)
  void setEnabled(bool b) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_MetaDataBaseItemCall3 call = reinterpret_cast<Cuteqdesigner_internal_MetaDataBaseItemCall3>(taken[3]);
      call(this, b, &handled);
      if (handled) return;
    }
    qdesigner_internal::MetaDataBaseItem::setEnabled(b);
  }
};

//  qdesigner_internal::MetaDataBaseItem::MetaDataBaseItem(QObject *object)
extern "C" Q_DECL_EXPORT
qdesigner_internal::MetaDataBaseItem *ritual_ZN18qdesigner_internal16MetaDataBaseItemC1EP7QObject(
    QObject *object) {
  return new Cuteqdesigner_internal_MetaDataBaseItem(object);
}

//  qdesigner_internal::MetaDataBaseItem::~MetaDataBaseItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16MetaDataBaseItemD1Ev(
    qdesigner_internal::MetaDataBaseItem *self) {
  delete self;
}

//  QString qdesigner_internal::MetaDataBaseItem::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal16MetaDataBaseItem4nameEv(
    const qdesigner_internal::MetaDataBaseItem *self) {
  return new QString(self->name());
}

//  void qdesigner_internal::MetaDataBaseItem::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16MetaDataBaseItem7setNameERK7QString(
    qdesigner_internal::MetaDataBaseItem *self,
    const QString *name) {
  self->setName(*name);
}

//  QWidgetList qdesigner_internal::MetaDataBaseItem::tabOrder() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal16MetaDataBaseItem8tabOrderEv(
    const qdesigner_internal::MetaDataBaseItem *self) {
  return new QList<QWidget *>(self->tabOrder());
}

//  void qdesigner_internal::MetaDataBaseItem::setTabOrder(const QWidgetList
//      &tabOrder)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16MetaDataBaseItem11setTabOrderERK5QListIP7QWidgetE(
    qdesigner_internal::MetaDataBaseItem *self,
    const QList<QWidget *> *tabOrder) {
  self->setTabOrder(*tabOrder);
}

//  bool qdesigner_internal::MetaDataBaseItem::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal16MetaDataBaseItem7enabledEv(
    const qdesigner_internal::MetaDataBaseItem *self) {
  return self->enabled();
}

//  void qdesigner_internal::MetaDataBaseItem::setEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16MetaDataBaseItem10setEnabledEb(
    qdesigner_internal::MetaDataBaseItem *self,
    bool b) {
  self->setEnabled(b);
}

//  QString qdesigner_internal::MetaDataBaseItem::customClassName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal16MetaDataBaseItem15customClassNameEv(
    const qdesigner_internal::MetaDataBaseItem *self) {
  return new QString(self->customClassName());
}

//  void qdesigner_internal::MetaDataBaseItem::setCustomClassName(const
//      QString &customClassName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16MetaDataBaseItem18setCustomClassNameERK7QString(
    qdesigner_internal::MetaDataBaseItem *self,
    const QString *customClassName) {
  self->setCustomClassName(*customClassName);
}

//  QStringList qdesigner_internal::MetaDataBaseItem::fakeSlots() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal16MetaDataBaseItem9fakeSlotsEv(
    const qdesigner_internal::MetaDataBaseItem *self) {
  return new QList<QString>(self->fakeSlots());
}

//  void qdesigner_internal::MetaDataBaseItem::setFakeSlots(const QStringList
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16MetaDataBaseItem12setFakeSlotsERK5QListI7QStringE(
    qdesigner_internal::MetaDataBaseItem *self,
    const QList<QString> *a0) {
  self->setFakeSlots(*a0);
}

//  QStringList qdesigner_internal::MetaDataBaseItem::fakeSignals() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal16MetaDataBaseItem11fakeSignalsEv(
    const qdesigner_internal::MetaDataBaseItem *self) {
  return new QList<QString>(self->fakeSignals());
}

//  void qdesigner_internal::MetaDataBaseItem::setFakeSignals(const
//      QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16MetaDataBaseItem14setFakeSignalsERK5QListI7QStringE(
    qdesigner_internal::MetaDataBaseItem *self,
    const QList<QString> *a0) {
  self->setFakeSignals(*a0);
}

//  a Python function taken by a Cuteqdesigner_internal_MetaDataBaseItem, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_MetaDataBaseItem(
    qdesigner_internal::MetaDataBaseItem *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_MetaDataBaseItem *>(self)->take(key, call);
}

//  QString qdesigner_internal::MetaDataBaseItem::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18qdesigner_internal16MetaDataBaseItem4nameEv(
    const qdesigner_internal::MetaDataBaseItem *self) {
  return new QString(self->qdesigner_internal::MetaDataBaseItem::name());
}

//  void qdesigner_internal::MetaDataBaseItem::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal16MetaDataBaseItem7setNameERK7QString(
    qdesigner_internal::MetaDataBaseItem *self,
    const QString *name) {
  self->qdesigner_internal::MetaDataBaseItem::setName(*name);
}

//  bool qdesigner_internal::MetaDataBaseItem::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18qdesigner_internal16MetaDataBaseItem7enabledEv(
    const qdesigner_internal::MetaDataBaseItem *self) {
  return self->qdesigner_internal::MetaDataBaseItem::enabled();
}

//  void qdesigner_internal::MetaDataBaseItem::setEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal16MetaDataBaseItem10setEnabledEb(
    qdesigner_internal::MetaDataBaseItem *self,
    bool b) {
  self->qdesigner_internal::MetaDataBaseItem::setEnabled(b);
}
