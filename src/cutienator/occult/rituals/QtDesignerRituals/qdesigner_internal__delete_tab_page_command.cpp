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

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1078, as _ZN18qdesigner_internal16TabWidgetCommandC2EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline TabWidgetCommand::TabWidgetCommand(QDesignerFormWindowInterface *formWindow) :
    QDesignerFormWindowCommand(QString(), formWindow),
    m_index(-1)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1139, as _ZN18qdesigner_internal20DeleteTabPageCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void DeleteTabPageCommand::redo()
{
    removePage();
    cheapUpdate();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1145, as _ZN18qdesigner_internal20DeleteTabPageCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void DeleteTabPageCommand::undo()
{
    addPage();
    cheapUpdate();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1131, as _ZN18qdesigner_internal20DeleteTabPageCommandD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline DeleteTabPageCommand::~DeleteTabPageCommand() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1086, as _ZN18qdesigner_internal16TabWidgetCommand4initEP10QTabWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void TabWidgetCommand::init(QTabWidget *tabWidget)
{
    m_tabWidget = tabWidget;
    m_index = m_tabWidget->currentIndex();
    m_widget = m_tabWidget->widget(m_index);
    m_itemText = m_tabWidget->tabText(m_index);
    m_itemIcon = m_tabWidget->tabIcon(m_index);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1095, as _ZN18qdesigner_internal16TabWidgetCommand10removePageEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void TabWidgetCommand::removePage()
{
    m_tabWidget->removeTab(m_index);

    m_widget->hide();
    m_widget->setParent(formWindow());
    m_tabWidget->setCurrentIndex(qMin(m_index, m_tabWidget->count()));

    formWindow()->clearSelection();
    formWindow()->selectWidget(m_tabWidget, true);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1107, as _ZN18qdesigner_internal16TabWidgetCommand7addPageEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void TabWidgetCommand::addPage()
{
    m_widget->setParent(nullptr);
    m_tabWidget->insertTab(m_index, m_widget, m_itemIcon, m_itemText);
    m_widget->show();
    m_tabWidget->setCurrentIndex(m_index);

    QDesignerPropertySheetExtension *sheet = qt_extension<QDesignerPropertySheetExtension*>(formWindow()->core()->extensionManager(), m_tabWidget);
    if (sheet) {
        qdesigner_internal::PropertySheetStringValue itemText(m_itemText);
        sheet->setProperty(sheet->indexOf(u"currentTabText"_s),
                           QVariant::fromValue(itemText));
    }

    formWindow()->clearSelection();
    formWindow()->selectWidget(m_tabWidget, true);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1084, as _ZN18qdesigner_internal16TabWidgetCommandD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline TabWidgetCommand::~TabWidgetCommand() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1126, as _ZN18qdesigner_internal20DeleteTabPageCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline DeleteTabPageCommand::DeleteTabPageCommand(QDesignerFormWindowInterface *formWindow)
    : TabWidgetCommand(formWindow)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1133, as _ZN18qdesigner_internal20DeleteTabPageCommand4initEP10QTabWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void DeleteTabPageCommand::init(QTabWidget *tabWidget)
{
    TabWidgetCommand::init(tabWidget);
    setText(QApplication::translate("Command", "Delete Page"));
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::DeleteTabPageCommand that Python can take functions over in. Every qdesigner_internal::DeleteTabPageCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_DeleteTabPageCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_DeleteTabPageCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_DeleteTabPageCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_DeleteTabPageCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_DeleteTabPageCommand : public qdesigner_internal::DeleteTabPageCommand {
public:
  using qdesigner_internal::DeleteTabPageCommand::DeleteTabPageCommand;
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
  //  void qdesigner_internal::DeleteTabPageCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_DeleteTabPageCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_DeleteTabPageCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::DeleteTabPageCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::DeleteTabPageCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_DeleteTabPageCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_DeleteTabPageCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::DeleteTabPageCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_DeleteTabPageCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_DeleteTabPageCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_DeleteTabPageCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_DeleteTabPageCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::DeleteTabPageCommand::DeleteTabPageCommand(QDesignerF
//      ormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeleteTabPageCommand *ritual_ZN18qdesigner_internal20DeleteTabPageCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_DeleteTabPageCommand(formWindow);
}

//  qdesigner_internal::DeleteTabPageCommand::~DeleteTabPageCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20DeleteTabPageCommandD1Ev(
    qdesigner_internal::DeleteTabPageCommand *self) {
  delete self;
}

//  void qdesigner_internal::DeleteTabPageCommand::init(QTabWidget
//      *tabWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20DeleteTabPageCommand4initEP10QTabWidget(
    qdesigner_internal::DeleteTabPageCommand *self,
    QTabWidget *tabWidget) {
  self->init(tabWidget);
}

//  void qdesigner_internal::DeleteTabPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20DeleteTabPageCommand4redoEv(
    qdesigner_internal::DeleteTabPageCommand *self) {
  self->redo();
}

//  void qdesigner_internal::DeleteTabPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20DeleteTabPageCommand4undoEv(
    qdesigner_internal::DeleteTabPageCommand *self) {
  self->undo();
}

//  a Python function taken by a Cuteqdesigner_internal_DeleteTabPageCommand,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_DeleteTabPageCommand(
    qdesigner_internal::DeleteTabPageCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_DeleteTabPageCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::DeleteTabPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20DeleteTabPageCommand4redoEv(
    qdesigner_internal::DeleteTabPageCommand *self) {
  self->qdesigner_internal::DeleteTabPageCommand::redo();
}

//  void qdesigner_internal::DeleteTabPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal20DeleteTabPageCommand4undoEv(
    qdesigner_internal::DeleteTabPageCommand *self) {
  self->qdesigner_internal::DeleteTabPageCommand::undo();
}
