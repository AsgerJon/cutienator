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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
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

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1359, as _ZN18qdesigner_internal27AddStackedWidgetPageCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddStackedWidgetPageCommand::redo()
{
    addPage();
    cheapUpdate();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1365, as _ZN18qdesigner_internal27AddStackedWidgetPageCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddStackedWidgetPageCommand::undo()
{
    removePage();
    cheapUpdate();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1335, as _ZN18qdesigner_internal27AddStackedWidgetPageCommandD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline AddStackedWidgetPageCommand::~AddStackedWidgetPageCommand() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1249, as _ZN18qdesigner_internal20StackedWidgetCommand10removePageEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void StackedWidgetCommand::removePage()
{
    m_stackedWidget->removeWidget(m_stackedWidget->widget(m_index));

    m_widget->hide();
    m_widget->setParent(formWindow());

    formWindow()->clearSelection();
    formWindow()->selectWidget(m_stackedWidget, true);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1260, as _ZN18qdesigner_internal20StackedWidgetCommand7addPageEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void StackedWidgetCommand::addPage()
{
    m_stackedWidget->insertWidget(m_index, m_widget);

    m_widget->show();
    m_stackedWidget->setCurrentIndex(m_index);

    formWindow()->clearSelection();
    formWindow()->selectWidget(m_stackedWidget, true);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1240, as _ZN18qdesigner_internal20StackedWidgetCommandD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline StackedWidgetCommand::~StackedWidgetCommand() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1330, as _ZN18qdesigner_internal27AddStackedWidgetPageCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline AddStackedWidgetPageCommand::AddStackedWidgetPageCommand(QDesignerFormWindowInterface *formWindow)
    : StackedWidgetCommand(formWindow)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1337, as _ZN18qdesigner_internal27AddStackedWidgetPageCommand4initEP14QStackedWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddStackedWidgetPageCommand::init(QStackedWidget *stackedWidget)
{
    init(stackedWidget, InsertBefore);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1342, as _ZN18qdesigner_internal27AddStackedWidgetPageCommand4initEP14QStackedWidgetNS0_13InsertionModeE
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void AddStackedWidgetPageCommand::init(QStackedWidget *stackedWidget, InsertionMode mode)
{
    m_stackedWidget = stackedWidget;

    m_index = m_stackedWidget->currentIndex();
    if (mode == InsertAfter)
        m_index++;
    m_widget = new QDesignerWidget(formWindow(), m_stackedWidget);
    m_widget->setObjectName(u"page"_s);
    formWindow()->ensureUniqueObjectName(m_widget);

    setText(QApplication::translate("Command", "Insert Page"));

    QDesignerFormEditorInterface *core = formWindow()->core();
    core->metaDataBase()->add(m_widget);
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::AddStackedWidgetPageCommand that Python can take functions over in. Every qdesigner_internal::AddStackedWidgetPageCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_AddStackedWidgetPageCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_AddStackedWidgetPageCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_AddStackedWidgetPageCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_AddStackedWidgetPageCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_AddStackedWidgetPageCommand : public qdesigner_internal::AddStackedWidgetPageCommand {
public:
  using qdesigner_internal::AddStackedWidgetPageCommand::AddStackedWidgetPageCommand;
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
  //  void qdesigner_internal::AddStackedWidgetPageCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_AddStackedWidgetPageCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_AddStackedWidgetPageCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::AddStackedWidgetPageCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::AddStackedWidgetPageCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_AddStackedWidgetPageCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_AddStackedWidgetPageCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::AddStackedWidgetPageCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_AddStackedWidgetPageCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_AddStackedWidgetPageCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_AddStackedWidgetPageCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_AddStackedWidgetPageCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::AddStackedWidgetPageCommand::AddStackedWidgetPageComm
//      and(QDesignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::AddStackedWidgetPageCommand *ritual_ZN18qdesigner_internal27AddStackedWidgetPageCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_AddStackedWidgetPageCommand(formWindow);
}

//  qdesigner_internal::AddStackedWidgetPageCommand::~AddStackedWidgetPageCom
//      mand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal27AddStackedWidgetPageCommandD1Ev(
    qdesigner_internal::AddStackedWidgetPageCommand *self) {
  delete self;
}

//  void qdesigner_internal::AddStackedWidgetPageCommand::init(QStackedWidget
//      *stackedWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal27AddStackedWidgetPageCommand4initEP14QStackedWidget(
    qdesigner_internal::AddStackedWidgetPageCommand *self,
    QStackedWidget *stackedWidget) {
  self->init(stackedWidget);
}

//  void qdesigner_internal::AddStackedWidgetPageCommand::init(QStackedWidget
//      *stackedWidget, InsertionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal27AddStackedWidgetPageCommand4initEP14QStackedWidgetNS0_13InsertionModeE(
    qdesigner_internal::AddStackedWidgetPageCommand *self,
    QStackedWidget *stackedWidget,
    qdesigner_internal::AddStackedWidgetPageCommand::InsertionMode mode) {
  self->init(stackedWidget, mode);
}

//  void qdesigner_internal::AddStackedWidgetPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal27AddStackedWidgetPageCommand4redoEv(
    qdesigner_internal::AddStackedWidgetPageCommand *self) {
  self->redo();
}

//  void qdesigner_internal::AddStackedWidgetPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal27AddStackedWidgetPageCommand4undoEv(
    qdesigner_internal::AddStackedWidgetPageCommand *self) {
  self->undo();
}

//  a Python function taken by a
//      Cuteqdesigner_internal_AddStackedWidgetPageCommand, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_AddStackedWidgetPageCommand(
    qdesigner_internal::AddStackedWidgetPageCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_AddStackedWidgetPageCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::AddStackedWidgetPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal27AddStackedWidgetPageCommand4redoEv(
    qdesigner_internal::AddStackedWidgetPageCommand *self) {
  self->qdesigner_internal::AddStackedWidgetPageCommand::redo();
}

//  void qdesigner_internal::AddStackedWidgetPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal27AddStackedWidgetPageCommand4undoEv(
    qdesigner_internal::AddStackedWidgetPageCommand *self) {
  self->qdesigner_internal::AddStackedWidgetPageCommand::undo();
}
