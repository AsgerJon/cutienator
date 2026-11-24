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

//  A qdesigner_internal::DeleteContainerWidgetPageCommand that Python can take functions over in. Every qdesigner_internal::DeleteContainerWidgetPageCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_DeleteContainerWidgetPageCommand : public qdesigner_internal::DeleteContainerWidgetPageCommand {
public:
  using qdesigner_internal::DeleteContainerWidgetPageCommand::DeleteContainerWidgetPageCommand;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4redoEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4undoEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZNK12QUndoCommand2idEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand9mergeWithEPKS_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
    return false;
  }

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::DeleteContainerWidgetPageCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::DeleteContainerWidgetPageCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::DeleteContainerWidgetPageCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::DeleteContainerWidgetPageCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QUndoCommand::id();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  bool QUndoCommand::mergeWith(const QUndoCommand *other)
  bool mergeWith(const QUndoCommand *other) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_DeleteContainerWidgetPageCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  a Python function taken by a
//      Cuteqdesigner_internal_DeleteContainerWidgetPageCommand, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_DeleteContainerWidgetPageCommand(
    qdesigner_internal::DeleteContainerWidgetPageCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_DeleteContainerWidgetPageCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::DeleteContainerWidgetPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal32DeleteContainerWidgetPageCommand4redoEv(
    qdesigner_internal::DeleteContainerWidgetPageCommand *self) {
  self->qdesigner_internal::DeleteContainerWidgetPageCommand::redo();
}

//  void qdesigner_internal::DeleteContainerWidgetPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal32DeleteContainerWidgetPageCommand4undoEv(
    qdesigner_internal::DeleteContainerWidgetPageCommand *self) {
  self->qdesigner_internal::DeleteContainerWidgetPageCommand::undo();
}
