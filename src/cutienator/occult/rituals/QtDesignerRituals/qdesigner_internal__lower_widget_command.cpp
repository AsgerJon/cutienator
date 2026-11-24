//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on qdesigner_internal::LowerWidgetCommand may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_LowerWidgetCommand : qdesigner_internal::LowerWidgetCommand {
  using qdesigner_internal::LowerWidgetCommand::reorder;
};

//  A qdesigner_internal::LowerWidgetCommand that Python can take functions over in. Every qdesigner_internal::LowerWidgetCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*Cuteqdesigner_internal_LowerWidgetCommandCall0)(const void *, QWidget *, int *);
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_LowerWidgetCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_LowerWidgetCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_LowerWidgetCommandCall3)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_LowerWidgetCommandCall4)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_LowerWidgetCommand : public qdesigner_internal::LowerWidgetCommand {
public:
  using qdesigner_internal::LowerWidgetCommand::LowerWidgetCommand;
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

  //  void qdesigner_internal::LowerWidgetCommand::reorder(QWidget *widget)
  //      const
  void reorder(QWidget *widget) const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_LowerWidgetCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_LowerWidgetCommandCall0>(taken[0]);
      call(this, widget, &handled);
      if (handled) return;
    }
    qdesigner_internal::LowerWidgetCommand::reorder(widget);
  }

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::ChangeZOrderCommand::redo()
  void redo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_LowerWidgetCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_LowerWidgetCommandCall1>(taken[1]);
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
      Cuteqdesigner_internal_LowerWidgetCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_LowerWidgetCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_LowerWidgetCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_LowerWidgetCommandCall3>(taken[3]);
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
      Cuteqdesigner_internal_LowerWidgetCommandCall4 call = reinterpret_cast<Cuteqdesigner_internal_LowerWidgetCommandCall4>(taken[4]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  a Python function taken by a Cuteqdesigner_internal_LowerWidgetCommand,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_LowerWidgetCommand(
    qdesigner_internal::LowerWidgetCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_LowerWidgetCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::LowerWidgetCommand::reorder(QWidget *widget)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18qdesigner_internal18LowerWidgetCommand7reorderEP7QWidget(
    const qdesigner_internal::LowerWidgetCommand *self,
    QWidget *widget) {
  static_cast<const Ownqdesigner_internal_LowerWidgetCommand *>(self)->Ownqdesigner_internal_LowerWidgetCommand::reorder(
      widget);
}
