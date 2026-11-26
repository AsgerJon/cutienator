//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qwidget.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on qdesigner_internal::RaiseWidgetCommand may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_RaiseWidgetCommand : qdesigner_internal::RaiseWidgetCommand {
  using qdesigner_internal::RaiseWidgetCommand::reorder;
};

//  A qdesigner_internal::RaiseWidgetCommand that Python can take functions over in. Every qdesigner_internal::RaiseWidgetCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cuteqdesigner_internal_RaiseWidgetCommandCall0)(const void *, QWidget *, int *);
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_RaiseWidgetCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_RaiseWidgetCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_RaiseWidgetCommandCall3)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_RaiseWidgetCommandCall4)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_RaiseWidgetCommand : public qdesigner_internal::RaiseWidgetCommand {
public:
  using qdesigner_internal::RaiseWidgetCommand::RaiseWidgetCommand;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18qdesigner_internal19ChangeZOrderCommand7reorderEP7QWidget")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4redoEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4undoEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZNK12QUndoCommand2idEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand9mergeWithEPKS_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
    return false;
  }

  //  void qdesigner_internal::RaiseWidgetCommand::reorder(QWidget *widget)
  //      const
  void reorder(QWidget *widget) const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_RaiseWidgetCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_RaiseWidgetCommandCall0>(taken[0]);
      call(this, widget, &handled);
      if (handled) return;
    }
    qdesigner_internal::RaiseWidgetCommand::reorder(widget);
  }

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::ChangeZOrderCommand::redo()
  void redo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_RaiseWidgetCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_RaiseWidgetCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::ChangeZOrderCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::ChangeZOrderCommand::undo()
  void undo() override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_RaiseWidgetCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_RaiseWidgetCommandCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::ChangeZOrderCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_RaiseWidgetCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_RaiseWidgetCommandCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QUndoCommand::id();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  bool QUndoCommand::mergeWith(const QUndoCommand *other)
  bool mergeWith(const QUndoCommand *other) override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_RaiseWidgetCommandCall4 call = reinterpret_cast<Cuteqdesigner_internal_RaiseWidgetCommandCall4>(taken[4]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::RaiseWidgetCommand::RaiseWidgetCommand(QDesignerFormW
//      indowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::RaiseWidgetCommand *ritual_ZN18qdesigner_internal18RaiseWidgetCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_RaiseWidgetCommand(formWindow);
}

//  void qdesigner_internal::RaiseWidgetCommand::init(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18RaiseWidgetCommand4initEP7QWidget(
    qdesigner_internal::RaiseWidgetCommand *self,
    QWidget *widget) {
  self->init(widget);
}

//  QWidgetList qdesigner_internal::RaiseWidgetCommand::reorderWidget(const
//      QWidgetList &list, QWidget *widget) const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal18RaiseWidgetCommand13reorderWidgetERK5QListIP7QWidgetES3_(
    const qdesigner_internal::RaiseWidgetCommand *self,
    const QList<QWidget *> *list,
    QWidget *widget) {
  return new QList<QWidget *>(self->reorderWidget(*list, widget));
}

//  void qdesigner_internal::RaiseWidgetCommand::reorder(QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal18RaiseWidgetCommand7reorderEP7QWidget(
    const qdesigner_internal::RaiseWidgetCommand *self,
    QWidget *widget) {
  self->reorder(widget);
}

//  a Python function taken by a Cuteqdesigner_internal_RaiseWidgetCommand,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_RaiseWidgetCommand(
    qdesigner_internal::RaiseWidgetCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_RaiseWidgetCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::RaiseWidgetCommand::reorder(QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18qdesigner_internal18RaiseWidgetCommand7reorderEP7QWidget(
    const qdesigner_internal::RaiseWidgetCommand *self,
    QWidget *widget) {
  static_cast<const Ownqdesigner_internal_RaiseWidgetCommand *>(self)->Ownqdesigner_internal_RaiseWidgetCommand::reorder(
      widget);
}
