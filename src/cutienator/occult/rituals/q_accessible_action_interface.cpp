//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>

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
