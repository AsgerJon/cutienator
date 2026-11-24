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

//  A qdesigner_internal::LayoutCommand that Python can take functions over in. Every qdesigner_internal::LayoutCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_LayoutCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_LayoutCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_LayoutCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_LayoutCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_LayoutCommand : public qdesigner_internal::LayoutCommand {
public:
  using qdesigner_internal::LayoutCommand::LayoutCommand;
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
  //  void qdesigner_internal::LayoutCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::LayoutCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::LayoutCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::LayoutCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_LayoutCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_LayoutCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  QWidgetList qdesigner_internal::LayoutCommand::widgets() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal13LayoutCommand7widgetsEv(
    const qdesigner_internal::LayoutCommand *self) {
  return new QList<QWidget *>(self->widgets());
}

//  a Python function taken by a Cuteqdesigner_internal_LayoutCommand, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_LayoutCommand(
    qdesigner_internal::LayoutCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_LayoutCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::LayoutCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal13LayoutCommand4redoEv(
    qdesigner_internal::LayoutCommand *self) {
  self->qdesigner_internal::LayoutCommand::redo();
}

//  void qdesigner_internal::LayoutCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal13LayoutCommand4undoEv(
    qdesigner_internal::LayoutCommand *self) {
  self->qdesigner_internal::LayoutCommand::undo();
}
