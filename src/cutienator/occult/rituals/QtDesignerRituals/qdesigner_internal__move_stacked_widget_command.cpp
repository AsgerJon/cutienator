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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/qdesigner_command_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/private/layout_p.h>
#include <QtDesigner/private/qlayout_widget_p.h>
#include <QtDesigner/private/qdesigner_widget_p.h>
#include <QtDesigner/private/qdesigner_menu_p.h>
#include <QtDesigner/private/shared_enums_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/formwindowbase_p.h>
#include <QtDesigner/abstractformbuilder.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/propertysheet.h>
#include <QtDesigner/abstractactioneditor.h>
#include <QtDesigner/abstractpropertyeditor.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/container.h>
#include <QtDesigner/layoutdecoration.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/abstractobjectinspector.h>
#include <QtDesigner/abstractintegration.h>
#include <QtDesigner/abstractformwindowcursor.h>
#include <QtCore/qdebug.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qqueue.h>
#include <QtWidgets/qmenubar.h>
#include <QtWidgets/qstatusbar.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qtoolbox.h>
#include <QtWidgets/qstackedwidget.h>
#include <QtWidgets/qtabwidget.h>
#include <QtWidgets/qtablewidget.h>
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qcombobox.h>
#include <QtWidgets/qsplitter.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qwizard.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qformlayout.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1234, as _ZN18qdesigner_internal20StackedWidgetCommandC2EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline StackedWidgetCommand::StackedWidgetCommand(QDesignerFormWindowInterface *formWindow) :
    QDesignerFormWindowCommand(QString(), formWindow),
    m_index(-1)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1291, as _ZN18qdesigner_internal24MoveStackedWidgetCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MoveStackedWidgetCommand::redo()
{
    m_stackedWidget->removeWidget(m_widget);
    m_stackedWidget->insertWidget(m_newIndex, m_widget);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1297, as _ZN18qdesigner_internal24MoveStackedWidgetCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MoveStackedWidgetCommand::undo()
{
    m_stackedWidget->removeWidget(m_widget);
    m_stackedWidget->insertWidget(m_oldIndex, m_widget);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1279, as _ZN18qdesigner_internal24MoveStackedWidgetCommandD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline MoveStackedWidgetCommand::~MoveStackedWidgetCommand() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1242, as _ZN18qdesigner_internal20StackedWidgetCommand4initEP14QStackedWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void StackedWidgetCommand::init(QStackedWidget *stackedWidget)
{
    m_stackedWidget = stackedWidget;
    m_index = m_stackedWidget->currentIndex();
    m_widget = m_stackedWidget->widget(m_index);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1281, as _ZN18qdesigner_internal24MoveStackedWidgetCommand4initEP14QStackedWidgetP7QWidgeti
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MoveStackedWidgetCommand::init(QStackedWidget *stackedWidget, QWidget *page, int newIndex)
{
    StackedWidgetCommand::init(stackedWidget);
    setText(QApplication::translate("Command", "Move Page"));

    m_widget = page;
    m_newIndex = newIndex;
    m_oldIndex = m_stackedWidget->indexOf(m_widget);
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::MoveStackedWidgetCommand that Python can take functions over in. Every qdesigner_internal::MoveStackedWidgetCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_MoveStackedWidgetCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_MoveStackedWidgetCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_MoveStackedWidgetCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_MoveStackedWidgetCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_MoveStackedWidgetCommand : public qdesigner_internal::MoveStackedWidgetCommand {
public:
  using qdesigner_internal::MoveStackedWidgetCommand::MoveStackedWidgetCommand;
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
  //  void qdesigner_internal::MoveStackedWidgetCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_MoveStackedWidgetCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_MoveStackedWidgetCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::MoveStackedWidgetCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::MoveStackedWidgetCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_MoveStackedWidgetCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_MoveStackedWidgetCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::MoveStackedWidgetCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_MoveStackedWidgetCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_MoveStackedWidgetCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_MoveStackedWidgetCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_MoveStackedWidgetCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::MoveStackedWidgetCommand::~MoveStackedWidgetCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24MoveStackedWidgetCommandD1Ev(
    qdesigner_internal::MoveStackedWidgetCommand *self) {
  delete self;
}

//  void qdesigner_internal::MoveStackedWidgetCommand::init(QStackedWidget
//      *stackedWidget, QWidget *page, int newIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24MoveStackedWidgetCommand4initEP14QStackedWidgetP7QWidgeti(
    qdesigner_internal::MoveStackedWidgetCommand *self,
    QStackedWidget *stackedWidget,
    QWidget *page,
    int newIndex) {
  self->init(stackedWidget, page, newIndex);
}

//  void qdesigner_internal::MoveStackedWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24MoveStackedWidgetCommand4redoEv(
    qdesigner_internal::MoveStackedWidgetCommand *self) {
  self->redo();
}

//  void qdesigner_internal::MoveStackedWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24MoveStackedWidgetCommand4undoEv(
    qdesigner_internal::MoveStackedWidgetCommand *self) {
  self->undo();
}

//  a Python function taken by a
//      Cuteqdesigner_internal_MoveStackedWidgetCommand, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_MoveStackedWidgetCommand(
    qdesigner_internal::MoveStackedWidgetCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_MoveStackedWidgetCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::MoveStackedWidgetCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal24MoveStackedWidgetCommand4redoEv(
    qdesigner_internal::MoveStackedWidgetCommand *self) {
  self->qdesigner_internal::MoveStackedWidgetCommand::redo();
}

//  void qdesigner_internal::MoveStackedWidgetCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal24MoveStackedWidgetCommand4undoEv(
    qdesigner_internal::MoveStackedWidgetCommand *self) {
  self->qdesigner_internal::MoveStackedWidgetCommand::undo();
}
