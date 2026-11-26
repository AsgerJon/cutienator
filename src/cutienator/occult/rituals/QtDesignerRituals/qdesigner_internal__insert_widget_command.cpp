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

//  A qdesigner_internal::InsertWidgetCommand that Python can take functions over in. Every qdesigner_internal::InsertWidgetCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_InsertWidgetCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_InsertWidgetCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_InsertWidgetCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_InsertWidgetCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_InsertWidgetCommand : public qdesigner_internal::InsertWidgetCommand {
public:
  using qdesigner_internal::InsertWidgetCommand::InsertWidgetCommand;
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
  //  void qdesigner_internal::InsertWidgetCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_InsertWidgetCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_InsertWidgetCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::InsertWidgetCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::InsertWidgetCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_InsertWidgetCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_InsertWidgetCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::InsertWidgetCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_InsertWidgetCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_InsertWidgetCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_InsertWidgetCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_InsertWidgetCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::InsertWidgetCommand::InsertWidgetCommand(QDesignerFor
//      mWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::InsertWidgetCommand *ritual_ZN18qdesigner_internal19InsertWidgetCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_InsertWidgetCommand(formWindow);
}

//  qdesigner_internal::InsertWidgetCommand::~InsertWidgetCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19InsertWidgetCommandD1Ev(
    qdesigner_internal::InsertWidgetCommand *self) {
  delete self;
}

//  void qdesigner_internal::InsertWidgetCommand::init(QWidget *widget, bool
//      already_in_form, int layoutRow, int layoutColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19InsertWidgetCommand4initEP7QWidgetbii(
    qdesigner_internal::InsertWidgetCommand *self,
    QWidget *widget,
    bool already_in_form,
    int layoutRow,
    int layoutColumn) {
  self->init(widget, already_in_form, layoutRow, layoutColumn);
}

//  void qdesigner_internal::InsertWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19InsertWidgetCommand4redoEv(
    qdesigner_internal::InsertWidgetCommand *self) {
  self->redo();
}

//  void qdesigner_internal::InsertWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19InsertWidgetCommand4undoEv(
    qdesigner_internal::InsertWidgetCommand *self) {
  self->undo();
}

//  void qdesigner_internal::InsertWidgetCommand::refreshBuddyLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19InsertWidgetCommand18refreshBuddyLabelsEv(
    qdesigner_internal::InsertWidgetCommand *self) {
  self->refreshBuddyLabels();
}

//  a Python function taken by a Cuteqdesigner_internal_InsertWidgetCommand,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_InsertWidgetCommand(
    qdesigner_internal::InsertWidgetCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_InsertWidgetCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::InsertWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal19InsertWidgetCommand4redoEv(
    qdesigner_internal::InsertWidgetCommand *self) {
  self->qdesigner_internal::InsertWidgetCommand::redo();
}

//  void qdesigner_internal::InsertWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal19InsertWidgetCommand4undoEv(
    qdesigner_internal::InsertWidgetCommand *self) {
  self->qdesigner_internal::InsertWidgetCommand::undo();
}
