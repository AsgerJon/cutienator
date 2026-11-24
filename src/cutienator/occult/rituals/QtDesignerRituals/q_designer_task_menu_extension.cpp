//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/taskmenu.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/taskmenu.h>
#include <QtGui/qaction.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerTaskMenuExtension that Python can take functions over in. Every QDesignerTaskMenuExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerTaskMenuExtensionCall0)(const void *, int *);
class CuteQDesignerTaskMenuExtension : public QDesignerTaskMenuExtension {
public:
  using QDesignerTaskMenuExtension::QDesignerTaskMenuExtension;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QDesignerTaskMenuExtension19preferredEditActionEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QAction *QDesignerTaskMenuExtension::preferredEditAction() const
  QAction *preferredEditAction() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerTaskMenuExtensionCall0 call = reinterpret_cast<CuteQDesignerTaskMenuExtensionCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return QDesignerTaskMenuExtension::preferredEditAction();
  }
};

//  QDesignerTaskMenuExtension::~QDesignerTaskMenuExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDesignerTaskMenuExtensionD1Ev(
    QDesignerTaskMenuExtension *self) {
  delete self;
}

//  QAction *QDesignerTaskMenuExtension::preferredEditAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK26QDesignerTaskMenuExtension19preferredEditActionEv(
    const QDesignerTaskMenuExtension *self) {
  return self->preferredEditAction();
}

//  QList<QAction *> QDesignerTaskMenuExtension::taskActions() const
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZNK26QDesignerTaskMenuExtension11taskActionsEv(
    const QDesignerTaskMenuExtension *self) {
  return new QList<QAction *>(self->taskActions());
}

//  a Python function taken by a CuteQDesignerTaskMenuExtension, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerTaskMenuExtension(
    QDesignerTaskMenuExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerTaskMenuExtension *>(self)->take(key, call);
}

//  QAction *QDesignerTaskMenuExtension::preferredEditAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_own_ZNK26QDesignerTaskMenuExtension19preferredEditActionEv(
    const QDesignerTaskMenuExtension *self) {
  return self->QDesignerTaskMenuExtension::preferredEditAction();
}
