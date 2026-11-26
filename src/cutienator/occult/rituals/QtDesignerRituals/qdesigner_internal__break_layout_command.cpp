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

//  A qdesigner_internal::BreakLayoutCommand that Python can take functions over in. Every qdesigner_internal::BreakLayoutCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_BreakLayoutCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_BreakLayoutCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_BreakLayoutCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_BreakLayoutCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_BreakLayoutCommand : public qdesigner_internal::BreakLayoutCommand {
public:
  using qdesigner_internal::BreakLayoutCommand::BreakLayoutCommand;
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
  //  void qdesigner_internal::BreakLayoutCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_BreakLayoutCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_BreakLayoutCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::BreakLayoutCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::BreakLayoutCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_BreakLayoutCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_BreakLayoutCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::BreakLayoutCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_BreakLayoutCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_BreakLayoutCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_BreakLayoutCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_BreakLayoutCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::BreakLayoutCommand::BreakLayoutCommand(QDesignerFormW
//      indowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::BreakLayoutCommand *ritual_ZN18qdesigner_internal18BreakLayoutCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_BreakLayoutCommand(formWindow);
}

//  qdesigner_internal::BreakLayoutCommand::~BreakLayoutCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18BreakLayoutCommandD1Ev(
    qdesigner_internal::BreakLayoutCommand *self) {
  delete self;
}

//  QWidgetList qdesigner_internal::BreakLayoutCommand::widgets() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK18qdesigner_internal18BreakLayoutCommand7widgetsEv(
    const qdesigner_internal::BreakLayoutCommand *self) {
  return new QList<QWidget *>(self->widgets());
}

//  void qdesigner_internal::BreakLayoutCommand::init(const QWidgetList
//      &widgets, QWidget *layoutBase, bool reparentLayoutWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18BreakLayoutCommand4initERK5QListIP7QWidgetES3_b(
    qdesigner_internal::BreakLayoutCommand *self,
    const QList<QWidget *> *widgets,
    QWidget *layoutBase,
    bool reparentLayoutWidget) {
  self->init(*widgets, layoutBase, reparentLayoutWidget);
}

//  void qdesigner_internal::BreakLayoutCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18BreakLayoutCommand4redoEv(
    qdesigner_internal::BreakLayoutCommand *self) {
  self->redo();
}

//  void qdesigner_internal::BreakLayoutCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18BreakLayoutCommand4undoEv(
    qdesigner_internal::BreakLayoutCommand *self) {
  self->undo();
}

//  const LayoutProperties
//      *qdesigner_internal::BreakLayoutCommand::layoutProperties() const
extern "C" Q_DECL_EXPORT
const qdesigner_internal::LayoutProperties *ritual_ZNK18qdesigner_internal18BreakLayoutCommand16layoutPropertiesEv(
    const qdesigner_internal::BreakLayoutCommand *self) {
  return self->layoutProperties();
}

//  int qdesigner_internal::BreakLayoutCommand::propertyMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal18BreakLayoutCommand12propertyMaskEv(
    const qdesigner_internal::BreakLayoutCommand *self) {
  return self->propertyMask();
}

//  a Python function taken by a Cuteqdesigner_internal_BreakLayoutCommand,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_BreakLayoutCommand(
    qdesigner_internal::BreakLayoutCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_BreakLayoutCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::BreakLayoutCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18BreakLayoutCommand4redoEv(
    qdesigner_internal::BreakLayoutCommand *self) {
  self->qdesigner_internal::BreakLayoutCommand::redo();
}

//  void qdesigner_internal::BreakLayoutCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18BreakLayoutCommand4undoEv(
    qdesigner_internal::BreakLayoutCommand *self) {
  self->qdesigner_internal::BreakLayoutCommand::undo();
}
