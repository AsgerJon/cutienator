//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAccessibleActionInterface that Python can take functions over in. Every QAccessibleActionInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQAccessibleActionInterfaceCall0)(const void *, const QString *, int *);
typedef QString * (*CuteQAccessibleActionInterfaceCall1)(const void *, const QString *, int *);
typedef void (*CuteQAccessibleActionInterfaceCall2)(const void *, const QString *, int *);
class CuteQAccessibleActionInterface : public QAccessibleActionInterface {
public:
  using QAccessibleActionInterface::QAccessibleActionInterface;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleActionInterfaceCall0 call = reinterpret_cast<CuteQAccessibleActionInterfaceCall0>(taken[0]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }

  //  QString QAccessibleActionInterface::localizedActionDescription(const
  //      QString &name) const
  QString localizedActionDescription(const QString &name) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleActionInterfaceCall1 call = reinterpret_cast<CuteQAccessibleActionInterfaceCall1>(taken[1]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionDescription(name);
  }

  //  void QAccessibleActionInterface::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleActionInterfaceCall2 call = reinterpret_cast<CuteQAccessibleActionInterfaceCall2>(taken[2]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
  }
};

//  QString QAccessibleActionInterface::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QAccessibleActionInterface::tr(
          sourceText,
          disambiguation,
          n));
}

//  QAccessibleActionInterface::~QAccessibleActionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleActionInterfaceD1Ev(
    QAccessibleActionInterface *self) {
  delete self;
}

//  QStringList QAccessibleActionInterface::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QAccessibleActionInterface11actionNamesEv(
    const QAccessibleActionInterface *self) {
  return new QList<QString>(self->actionNames());
}

//  QString QAccessibleActionInterface::localizedActionName(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString(
    const QAccessibleActionInterface *self,
    const QString *name) {
  return new QString(self->localizedActionName(*name));
}

//  QString QAccessibleActionInterface::localizedActionDescription(const
//      QString &name) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString(
    const QAccessibleActionInterface *self,
    const QString *name) {
  return new QString(self->localizedActionDescription(*name));
}

//  void QAccessibleActionInterface::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleActionInterface8doActionERK7QString(
    QAccessibleActionInterface *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QStringList QAccessibleActionInterface::keyBindingsForAction(const
//      QString &actionName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QAccessibleActionInterface20keyBindingsForActionERK7QString(
    const QAccessibleActionInterface *self,
    const QString *actionName) {
  return new QList<QString>(self->keyBindingsForAction(*actionName));
}

//  const QString &QAccessibleActionInterface::pressAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface11pressActionEv() {
  return new QString(QAccessibleActionInterface::pressAction());
}

//  const QString &QAccessibleActionInterface::increaseAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface14increaseActionEv() {
  return new QString(QAccessibleActionInterface::increaseAction());
}

//  const QString &QAccessibleActionInterface::decreaseAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface14decreaseActionEv() {
  return new QString(QAccessibleActionInterface::decreaseAction());
}

//  const QString &QAccessibleActionInterface::showMenuAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface14showMenuActionEv() {
  return new QString(QAccessibleActionInterface::showMenuAction());
}

//  const QString &QAccessibleActionInterface::setFocusAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface14setFocusActionEv() {
  return new QString(QAccessibleActionInterface::setFocusAction());
}

//  const QString &QAccessibleActionInterface::showOnScreenAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface18showOnScreenActionEv() {
  return new QString(QAccessibleActionInterface::showOnScreenAction());
}

//  const QString &QAccessibleActionInterface::toggleAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface12toggleActionEv() {
  return new QString(QAccessibleActionInterface::toggleAction());
}

//  QString QAccessibleActionInterface::scrollLeftAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface16scrollLeftActionEv() {
  return new QString(QAccessibleActionInterface::scrollLeftAction());
}

//  QString QAccessibleActionInterface::scrollRightAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface17scrollRightActionEv() {
  return new QString(QAccessibleActionInterface::scrollRightAction());
}

//  QString QAccessibleActionInterface::scrollUpAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface14scrollUpActionEv() {
  return new QString(QAccessibleActionInterface::scrollUpAction());
}

//  QString QAccessibleActionInterface::scrollDownAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface16scrollDownActionEv() {
  return new QString(QAccessibleActionInterface::scrollDownAction());
}

//  QString QAccessibleActionInterface::nextPageAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface14nextPageActionEv() {
  return new QString(QAccessibleActionInterface::nextPageAction());
}

//  QString QAccessibleActionInterface::previousPageAction()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAccessibleActionInterface18previousPageActionEv() {
  return new QString(QAccessibleActionInterface::previousPageAction());
}

//  a Python function taken by a CuteQAccessibleActionInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleActionInterface(
    QAccessibleActionInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleActionInterface *>(self)->take(key, call);
}

//  QString QAccessibleActionInterface::localizedActionName(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString(
    const QAccessibleActionInterface *self,
    const QString *name) {
  return new QString(
      self->QAccessibleActionInterface::localizedActionName(
          *name));
}

//  QString QAccessibleActionInterface::localizedActionDescription(const
//      QString &name) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString(
    const QAccessibleActionInterface *self,
    const QString *name) {
  return new QString(
      self->QAccessibleActionInterface::localizedActionDescription(
          *name));
}
