//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command2_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A qdesigner_internal::MorphLayoutCommand that Python can take functions over in. Every qdesigner_internal::MorphLayoutCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_MorphLayoutCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_MorphLayoutCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_MorphLayoutCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_MorphLayoutCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_MorphLayoutCommand : public qdesigner_internal::MorphLayoutCommand {
public:
  using qdesigner_internal::MorphLayoutCommand::MorphLayoutCommand;
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
  //  void qdesigner_internal::MorphLayoutCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_MorphLayoutCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_MorphLayoutCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::MorphLayoutCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::MorphLayoutCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_MorphLayoutCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_MorphLayoutCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::MorphLayoutCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_MorphLayoutCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_MorphLayoutCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_MorphLayoutCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_MorphLayoutCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::MorphLayoutCommand::MorphLayoutCommand(QDesignerFormW
//      indowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::MorphLayoutCommand *ritual_ZN18qdesigner_internal18MorphLayoutCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_MorphLayoutCommand(formWindow);
}

//  qdesigner_internal::MorphLayoutCommand::~MorphLayoutCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MorphLayoutCommandD1Ev(
    qdesigner_internal::MorphLayoutCommand *self) {
  delete self;
}

//  bool qdesigner_internal::MorphLayoutCommand::init(QWidget *w, int
//      newType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18MorphLayoutCommand4initEP7QWidgeti(
    qdesigner_internal::MorphLayoutCommand *self,
    QWidget *w,
    int newType) {
  return self->init(w, newType);
}

//  bool qdesigner_internal::MorphLayoutCommand::canMorph(const
//      QDesignerFormWindowInterface *formWindow, QWidget *w, int
//      *ptrToCurrentType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal18MorphLayoutCommand8canMorphEPK28QDesignerFormWindowInterfaceP7QWidgetPi(
    const QDesignerFormWindowInterface *formWindow,
    QWidget *w,
    int *ptrToCurrentType) {
  return qdesigner_internal::MorphLayoutCommand::canMorph(
      formWindow,
      w,
      ptrToCurrentType);
}

//  void qdesigner_internal::MorphLayoutCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MorphLayoutCommand4redoEv(
    qdesigner_internal::MorphLayoutCommand *self) {
  self->redo();
}

//  void qdesigner_internal::MorphLayoutCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MorphLayoutCommand4undoEv(
    qdesigner_internal::MorphLayoutCommand *self) {
  self->undo();
}

//  QString qdesigner_internal::MorphLayoutCommand::formatDescription(QDesign
//      erFormEditorInterface *core, const QWidget *w, int oldType, int
//      newType)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal18MorphLayoutCommand17formatDescriptionEP28QDesignerFormEditorInterfacePK7QWidgetii(
    QDesignerFormEditorInterface *core,
    const QWidget *w,
    int oldType,
    int newType) {
  return new QString(
      qdesigner_internal::MorphLayoutCommand::formatDescription(
          core,
          w,
          oldType,
          newType));
}

//  a Python function taken by a Cuteqdesigner_internal_MorphLayoutCommand,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_MorphLayoutCommand(
    qdesigner_internal::MorphLayoutCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_MorphLayoutCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::MorphLayoutCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18MorphLayoutCommand4redoEv(
    qdesigner_internal::MorphLayoutCommand *self) {
  self->qdesigner_internal::MorphLayoutCommand::redo();
}

//  void qdesigner_internal::MorphLayoutCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18MorphLayoutCommand4undoEv(
    qdesigner_internal::MorphLayoutCommand *self) {
  self->qdesigner_internal::MorphLayoutCommand::undo();
}
