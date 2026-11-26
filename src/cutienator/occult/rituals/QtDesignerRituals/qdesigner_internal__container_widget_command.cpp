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

//  A qdesigner_internal::ContainerWidgetCommand that Python can take functions over in. Every qdesigner_internal::ContainerWidgetCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_ContainerWidgetCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_ContainerWidgetCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_ContainerWidgetCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_ContainerWidgetCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_ContainerWidgetCommand : public qdesigner_internal::ContainerWidgetCommand {
public:
  using qdesigner_internal::ContainerWidgetCommand::ContainerWidgetCommand;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4undoEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4redoEv")) {
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
  //  void qdesigner_internal::QDesignerFormWindowCommand::undo()
  void undo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_ContainerWidgetCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_ContainerWidgetCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::QDesignerFormWindowCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::QDesignerFormWindowCommand::redo()
  void redo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_ContainerWidgetCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_ContainerWidgetCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::QDesignerFormWindowCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_ContainerWidgetCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_ContainerWidgetCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_ContainerWidgetCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_ContainerWidgetCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::ContainerWidgetCommand::ContainerWidgetCommand(QDesig
//      nerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ContainerWidgetCommand *ritual_ZN18qdesigner_internal22ContainerWidgetCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_ContainerWidgetCommand(formWindow);
}

//  qdesigner_internal::ContainerWidgetCommand::~ContainerWidgetCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22ContainerWidgetCommandD1Ev(
    qdesigner_internal::ContainerWidgetCommand *self) {
  delete self;
}

//  QDesignerContainerExtension
//      *qdesigner_internal::ContainerWidgetCommand::containerExtension()
//      const
extern "C" Q_DECL_EXPORT
QDesignerContainerExtension *ritual_ZNK18qdesigner_internal22ContainerWidgetCommand18containerExtensionEv(
    const qdesigner_internal::ContainerWidgetCommand *self) {
  return self->containerExtension();
}

//  void qdesigner_internal::ContainerWidgetCommand::init(QWidget
//      *containerWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22ContainerWidgetCommand4initEP7QWidget(
    qdesigner_internal::ContainerWidgetCommand *self,
    QWidget *containerWidget) {
  self->init(containerWidget);
}

//  void qdesigner_internal::ContainerWidgetCommand::removePage()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22ContainerWidgetCommand10removePageEv(
    qdesigner_internal::ContainerWidgetCommand *self) {
  self->removePage();
}

//  void qdesigner_internal::ContainerWidgetCommand::addPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22ContainerWidgetCommand7addPageEv(
    qdesigner_internal::ContainerWidgetCommand *self) {
  self->addPage();
}

//  a Python function taken by a
//      Cuteqdesigner_internal_ContainerWidgetCommand, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_ContainerWidgetCommand(
    qdesigner_internal::ContainerWidgetCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_ContainerWidgetCommand *>(self)->take(key, call);
}
