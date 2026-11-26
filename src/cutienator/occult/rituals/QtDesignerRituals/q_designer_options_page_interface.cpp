//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractoptionspage.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractoptionspage.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerOptionsPageInterface that Python can take functions over in. Every QDesignerOptionsPageInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQDesignerOptionsPageInterfaceCall0)(const void *, int *);
typedef void * (*CuteQDesignerOptionsPageInterfaceCall1)(const void *, QWidget *, int *);
typedef void (*CuteQDesignerOptionsPageInterfaceCall2)(const void *, int *);
typedef void (*CuteQDesignerOptionsPageInterfaceCall3)(const void *, int *);
class CuteQDesignerOptionsPageInterface : public QDesignerOptionsPageInterface {
public:
  using QDesignerOptionsPageInterface::QDesignerOptionsPageInterface;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QDesignerOptionsPageInterface4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerOptionsPageInterface10createPageEP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerOptionsPageInterface5applyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QDesignerOptionsPageInterface6finishEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QString QDesignerOptionsPageInterface::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerOptionsPageInterfaceCall0 call = reinterpret_cast<CuteQDesignerOptionsPageInterfaceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QWidget *QDesignerOptionsPageInterface::createPage(QWidget *parent)
  QWidget *createPage(QWidget *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerOptionsPageInterfaceCall1 call = reinterpret_cast<CuteQDesignerOptionsPageInterfaceCall1>(taken[1]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  void QDesignerOptionsPageInterface::apply()
  void apply() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerOptionsPageInterfaceCall2 call = reinterpret_cast<CuteQDesignerOptionsPageInterfaceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDesignerOptionsPageInterface::finish()
  void finish() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerOptionsPageInterfaceCall3 call = reinterpret_cast<CuteQDesignerOptionsPageInterfaceCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QDesignerOptionsPageInterface::QDesignerOptionsPageInterface()
extern "C" Q_DECL_EXPORT
QDesignerOptionsPageInterface *ritual_ZN29QDesignerOptionsPageInterfaceC1Ev() {
  return new CuteQDesignerOptionsPageInterface();
}

//  QDesignerOptionsPageInterface::~QDesignerOptionsPageInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerOptionsPageInterfaceD1Ev(
    QDesignerOptionsPageInterface *self) {
  delete self;
}

//  QString QDesignerOptionsPageInterface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDesignerOptionsPageInterface4nameEv(
    const QDesignerOptionsPageInterface *self) {
  return new QString(self->name());
}

//  QWidget *QDesignerOptionsPageInterface::createPage(QWidget *parent)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN29QDesignerOptionsPageInterface10createPageEP7QWidget(
    QDesignerOptionsPageInterface *self,
    QWidget *parent) {
  return self->createPage(parent);
}

//  void QDesignerOptionsPageInterface::apply()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerOptionsPageInterface5applyEv(
    QDesignerOptionsPageInterface *self) {
  self->apply();
}

//  void QDesignerOptionsPageInterface::finish()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDesignerOptionsPageInterface6finishEv(
    QDesignerOptionsPageInterface *self) {
  self->finish();
}

//  a Python function taken by a CuteQDesignerOptionsPageInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerOptionsPageInterface(
    QDesignerOptionsPageInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerOptionsPageInterface *>(self)->take(key, call);
}

//  QList<QDesignerOptionsPageInterface *>::QList()
extern "C" Q_DECL_EXPORT
QList<QDesignerOptionsPageInterface *> *ritual_list_make_QDesignerOptionsPageInterface_ptr() {
  return new QList<QDesignerOptionsPageInterface *>();
}

//  void QList<QDesignerOptionsPageInterface *>::append(const
//      QDesignerOptionsPageInterface * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDesignerOptionsPageInterface_ptr(
    QList<QDesignerOptionsPageInterface *> *self,
    QDesignerOptionsPageInterface *element) {
  self->append(element);
}

//  qsizetype QList<QDesignerOptionsPageInterface *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDesignerOptionsPageInterface_ptr(
    const QList<QDesignerOptionsPageInterface *> *self) {
  return self->size();
}

//  const QDesignerOptionsPageInterface *
//      &QList<QDesignerOptionsPageInterface *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDesignerOptionsPageInterface *ritual_list_at_QDesignerOptionsPageInterface_ptr(
    const QList<QDesignerOptionsPageInterface *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QDesignerOptionsPageInterface *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDesignerOptionsPageInterface_ptr(
    QList<QDesignerOptionsPageInterface *> *self) {
  delete self;
}
