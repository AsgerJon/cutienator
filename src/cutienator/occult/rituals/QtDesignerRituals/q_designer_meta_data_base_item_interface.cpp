//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractmetadatabase.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractmetadatabase.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerMetaDataBaseItemInterface that Python can take functions over in. Every QDesignerMetaDataBaseItemInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQDesignerMetaDataBaseItemInterfaceCall0)(const void *, int *);
typedef void (*CuteQDesignerMetaDataBaseItemInterfaceCall1)(const void *, const QString *, int *);
typedef bool (*CuteQDesignerMetaDataBaseItemInterfaceCall2)(const void *, int *);
typedef void (*CuteQDesignerMetaDataBaseItemInterfaceCall3)(const void *, bool, int *);
class CuteQDesignerMetaDataBaseItemInterface : public QDesignerMetaDataBaseItemInterface {
public:
  using QDesignerMetaDataBaseItemInterface::QDesignerMetaDataBaseItemInterface;
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

  //  QString QDesignerMetaDataBaseItemInterface::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseItemInterfaceCall0 call = reinterpret_cast<CuteQDesignerMetaDataBaseItemInterfaceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QDesignerMetaDataBaseItemInterface::setName(const QString &name)
  void setName(const QString &name) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseItemInterfaceCall1 call = reinterpret_cast<CuteQDesignerMetaDataBaseItemInterfaceCall1>(taken[1]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }

  //  bool QDesignerMetaDataBaseItemInterface::enabled() const
  bool enabled() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseItemInterfaceCall2 call = reinterpret_cast<CuteQDesignerMetaDataBaseItemInterfaceCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerMetaDataBaseItemInterface::setEnabled(bool b)
  void setEnabled(bool b) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerMetaDataBaseItemInterfaceCall3 call = reinterpret_cast<CuteQDesignerMetaDataBaseItemInterfaceCall3>(taken[3]);
      call(this, b, &handled);
      if (handled) return;
    }
  }
};

//  QDesignerMetaDataBaseItemInterface::~QDesignerMetaDataBaseItemInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerMetaDataBaseItemInterfaceD1Ev(
    QDesignerMetaDataBaseItemInterface *self) {
  delete self;
}

//  QString QDesignerMetaDataBaseItemInterface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK34QDesignerMetaDataBaseItemInterface4nameEv(
    const QDesignerMetaDataBaseItemInterface *self) {
  return new QString(self->name());
}

//  void QDesignerMetaDataBaseItemInterface::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerMetaDataBaseItemInterface7setNameERK7QString(
    QDesignerMetaDataBaseItemInterface *self,
    const QString *name) {
  self->setName(*name);
}

//  QList<QWidget *> QDesignerMetaDataBaseItemInterface::tabOrder() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK34QDesignerMetaDataBaseItemInterface8tabOrderEv(
    const QDesignerMetaDataBaseItemInterface *self) {
  return new QList<QWidget *>(self->tabOrder());
}

//  void QDesignerMetaDataBaseItemInterface::setTabOrder(const QList<QWidget
//      *> &tabOrder)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerMetaDataBaseItemInterface11setTabOrderERK5QListIP7QWidgetE(
    QDesignerMetaDataBaseItemInterface *self,
    const QList<QWidget *> *tabOrder) {
  self->setTabOrder(*tabOrder);
}

//  bool QDesignerMetaDataBaseItemInterface::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QDesignerMetaDataBaseItemInterface7enabledEv(
    const QDesignerMetaDataBaseItemInterface *self) {
  return self->enabled();
}

//  void QDesignerMetaDataBaseItemInterface::setEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerMetaDataBaseItemInterface10setEnabledEb(
    QDesignerMetaDataBaseItemInterface *self,
    bool b) {
  self->setEnabled(b);
}

//  a Python function taken by a CuteQDesignerMetaDataBaseItemInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerMetaDataBaseItemInterface(
    QDesignerMetaDataBaseItemInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerMetaDataBaseItemInterface *>(self)->take(key, call);
}
