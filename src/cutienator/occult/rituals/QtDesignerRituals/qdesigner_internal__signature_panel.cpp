//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'qdesigner_internal::SignaturePanel' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDesigner/private/signalslotdialog_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/widgetdatabase_p.h>
#include <QtDesigner/private/qdesigner_formwindowcommand_p.h>
#include <QtDesigner/private/iconloader_p.h>
#include <QtDesigner/membersheet.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/private/abstractdialoggui_p.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qvalidator.h>
#include <QtWidgets/qstyleditemdelegate.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qmessagebox.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 36, as local:signalslotdialog.cpp:signatureRegExp
static constexpr auto signatureRegExp = "^[\\w+_]+\\(([\\w+:]\\*?,?)*\\)$"_L1;

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 37, as local:signalslotdialog.cpp:methodNameRegExp
static constexpr auto methodNameRegExp = "^[\\w+_]+$"_L1;

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 39, as local:signalslotdialog.cpp:createEditableItem
static QStandardItem *createEditableItem(const QString &text)
{
    QStandardItem *rc = new QStandardItem(text);
    rc->setFlags(Qt::ItemIsEnabled|Qt::ItemIsEditable|Qt::ItemIsSelectable);
    return rc;
}

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 46, as local:signalslotdialog.cpp:createDisabledItem
static QStandardItem *createDisabledItem(const QString &text)
{
    QStandardItem *rc = new QStandardItem(text);
    Qt::ItemFlags flags = rc->flags();
    rc->setFlags(flags & ~(Qt::ItemIsEnabled|Qt::ItemIsEditable|Qt::ItemIsSelectable));
    return rc;
}

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 57, as local:signalslotdialog.cpp:SignatureDelegate
namespace {
class SignatureDelegate : public QStyledItemDelegate {
    public:
        SignatureDelegate(QObject * parent = nullptr);
        QWidget * createEditor (QWidget * parent, const QStyleOptionViewItem &option, const QModelIndex &index ) const override;
        void setModelData (QWidget *editor, QAbstractItemModel *model, const QModelIndex &index) const override;

    private:
        const QRegularExpression m_signatureRegexp;
        const QRegularExpression m_methodNameRegexp;
    };
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 68, as local:signalslotdialog.cpp:SignatureDelegate::SignatureDelegate
namespace {
inline SignatureDelegate::SignatureDelegate(QObject * parent) :
        QStyledItemDelegate(parent),
        m_signatureRegexp(signatureRegExp),
        m_methodNameRegexp(methodNameRegExp)
    {
        Q_ASSERT(m_signatureRegexp.isValid());
        Q_ASSERT(m_methodNameRegexp.isValid());
    }
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 77, as local:signalslotdialog.cpp:SignatureDelegate::createEditor
namespace {
inline QWidget * SignatureDelegate::createEditor ( QWidget * parent, const QStyleOptionViewItem &option, const QModelIndex &index ) const
    {
        QWidget *rc = QStyledItemDelegate::createEditor(parent, option, index);
        QLineEdit *le = qobject_cast<QLineEdit *>(rc);
        Q_ASSERT(le);
        le->setValidator(new QRegularExpressionValidator(m_signatureRegexp, le));
        return rc;
    }
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 86, as local:signalslotdialog.cpp:SignatureDelegate::setModelData
namespace {
inline void SignatureDelegate::setModelData(QWidget *editor, QAbstractItemModel *model, const QModelIndex &index ) const
    {
        QLineEdit *le = qobject_cast<QLineEdit *>(editor);
        Q_ASSERT(le);
        // Did the user just type a name? .. Add parentheses
        QString signature = le->text();
        if (!m_signatureRegexp.match(signature).hasMatch()) {
            if (m_methodNameRegexp.match(signature).hasMatch()) {
                signature += "()"_L1;
                le->setText(signature);
            } else {
                return;
            }
        }
        QStyledItemDelegate::setModelData(editor, model, index);
    }
}  // namespace

//  from QtDesigner__qdesigner_internal_SignaturePanel.cpp, line 1, as moc:qdesigner_internal::SignaturePanel
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18qdesigner_internal14SignaturePanelE_t {};
} // unnamed namespace

template <> constexpr inline auto qdesigner_internal::SignaturePanel::qt_create_metaobjectdata<qt_meta_tag_ZN18qdesigner_internal14SignaturePanelE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "qdesigner_internal::SignaturePanel",
        "checkSignature",
        "",
        "signature",
        "bool*",
        "ok",
        "slotAdd",
        "slotRemove",
        "slotSelectionChanged",
        "QItemSelection"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'checkSignature'
        QtMocHelpers::SignalData<void(const QString &, bool *)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 3 }, { 0x80000000 | 4, 5 },
        }}),
        // Slot 'slotAdd'
        QtMocHelpers::SlotData<void()>(6, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'slotRemove'
        QtMocHelpers::SlotData<void()>(7, 2, QMC::AccessPrivate, QMetaType::Void),
        // Slot 'slotSelectionChanged'
        QtMocHelpers::SlotData<void(const QItemSelection &, const QItemSelection &)>(8, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 9, 2 }, { 0x80000000 | 9, 2 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<SignaturePanel, qt_meta_tag_ZN18qdesigner_internal14SignaturePanelE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject qdesigner_internal::SignaturePanel::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14SignaturePanelE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14SignaturePanelE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18qdesigner_internal14SignaturePanelE_t>.metaTypes,
    nullptr
} };

void qdesigner_internal::SignaturePanel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<SignaturePanel *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->checkSignature((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<bool*>>(_a[2]))); break;
        case 1: _t->slotAdd(); break;
        case 2: _t->slotRemove(); break;
        case 3: _t->slotSelectionChanged((*reinterpret_cast<std::add_pointer_t<QItemSelection>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QItemSelection>>(_a[2]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (SignaturePanel::*)(const QString & , bool * )>(_a, &SignaturePanel::checkSignature, 0))
            return;
    }
}

const QMetaObject *qdesigner_internal::SignaturePanel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *qdesigner_internal::SignaturePanel::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14SignaturePanelE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int qdesigner_internal::SignaturePanel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 4;
    }
    return _id;
}

// SIGNAL 0
void qdesigner_internal::SignaturePanel::checkSignature(const QString & _t1, bool * _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1, _t2);
}
QT_WARNING_POP

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 231, as _ZN18qdesigner_internal14SignaturePanel10slotRemoveEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void SignaturePanel::slotRemove()
{
    const QModelIndexList selectedIndexes = m_listView->selectionModel()->selectedIndexes ();
    if (selectedIndexes.isEmpty())
        return;

    closeEditor();
    // scroll to previous
    if (const int row = selectedIndexes.constFirst().row())
        m_listView->setCurrentIndex (selectedIndexes.constFirst().sibling(row - 1, 0));

    for (auto i = selectedIndexes.size() - 1; i >= 0; --i)
        qDeleteAll(m_model->takeRow(selectedIndexes.at(i).row()));
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 246, as _ZN18qdesigner_internal14SignaturePanel20slotSelectionChangedERK14QItemSelectionS3_
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void SignaturePanel::slotSelectionChanged(const QItemSelection &selected, const QItemSelection &)
{
    m_removeButton->setEnabled(!selected.indexes().isEmpty());
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 206, as _ZN18qdesigner_internal14SignaturePanel7slotAddEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void SignaturePanel::slotAdd()
{
    m_listView->selectionModel()->clearSelection();
    // find unique name
    for (int i = 1; ; i++) {
        // Always add number, Avoid setting 'slot' for first entry
        QString newSlot = m_newPrefix + QString::number(i) + u'(';
        // check for function name independent of parameters
        if (m_model->findItems(newSlot, Qt::MatchStartsWith, 0).isEmpty()) {
            newSlot += u')';
            QStandardItem * item = createEditableItem(newSlot);
            m_model->appendRow(item);
            const  QModelIndex index = m_model->indexFromItem (item);
            m_listView->setCurrentIndex (index);
            m_listView->edit(index);
            return;
        }
    }
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 160, as _ZN18qdesigner_internal14SignatureModelC1EP7QObject
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline SignatureModel::SignatureModel(QObject *parent) :
     QStandardItemModel(parent)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 185, as _ZN18qdesigner_internal14SignaturePanelC1EP7QObjectP9QListViewP11QToolButtonS6_RK7QString
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline SignaturePanel::SignaturePanel(QObject *parent, QListView *listView, QToolButton *addButton, QToolButton *removeButton, const QString &newPrefix) :
    QObject(parent),
    m_newPrefix(newPrefix),
    m_model(new SignatureModel(this)),
    m_listView(listView),
    m_removeButton(removeButton)
{
    m_removeButton->setEnabled(false);

    connect(addButton, &QAbstractButton::clicked, this, &SignaturePanel::slotAdd);
    connect(m_removeButton, &QAbstractButton::clicked, this, &SignaturePanel::slotRemove);

    m_listView->setModel(m_model);
    SignatureDelegate *delegate = new SignatureDelegate(this);
    m_listView->setItemDelegate(delegate);
    connect(m_model, &SignatureModel::checkSignature,
            this, &SignaturePanel::checkSignature);
    connect(m_listView->selectionModel(), &QItemSelectionModel::selectionChanged,
            this, &SignaturePanel::slotSelectionChanged);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 266, as _ZNK18qdesigner_internal14SignaturePanel11fakeMethodsEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QStringList SignaturePanel::fakeMethods() const
{
    QStringList rc;
    if (const int rowCount = m_model->rowCount())
        for (int  i = 0; i < rowCount; i++) {
            const QStandardItem *item =  m_model->item(i);
            if (item->flags() & Qt::ItemIsEditable)
                rc += item->text();
        }
    return rc;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 251, as _ZN18qdesigner_internal14SignaturePanel7setDataERKNS_20SignalSlotDialogDataE
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void SignaturePanel::setData(const SignalSlotDialogData &d)
{
    m_model->clear();

    QStandardItem *lastExisting = nullptr;
    for (const QString &s : d.m_existingMethods) {
        lastExisting = createDisabledItem(s);
        m_model->appendRow(lastExisting);
    }
    for (const QString &s : d.m_fakeMethods)
        m_model->appendRow(createEditableItem(s));
    if (lastExisting)
        m_listView->scrollTo(m_model->indexFromItem(lastExisting));
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 226, as _ZNK18qdesigner_internal14SignaturePanel5countERK7QString
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline int SignaturePanel::count(const QString &signature) const
{
    return m_model->findItems(signature).size();
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/signalslotdialog.cpp, line 278, as _ZN18qdesigner_internal14SignaturePanel11closeEditorEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void SignaturePanel::closeEditor()
{
    const QModelIndex idx = m_listView->currentIndex();
    if (idx.isValid())
        m_listView->closePersistentEditor(idx);
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  const QMetaObject *qdesigner_internal::SignaturePanel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14SignaturePanel10metaObjectEv(
    const qdesigner_internal::SignaturePanel *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::SignaturePanel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14SignaturePanel11qt_metacastEPKc(
    qdesigner_internal::SignaturePanel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::SignaturePanel::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14SignaturePanel11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::SignaturePanel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::SignaturePanel::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14SignaturePanel2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::SignaturePanel::tr(s, c, n));
}

//  qdesigner_internal::SignaturePanel::SignaturePanel(QObject *parent,
//      QListView *listView, QToolButton *addButton, QToolButton
//      *removeButton, const QString &newPrefix)
extern "C" Q_DECL_EXPORT
qdesigner_internal::SignaturePanel *ritual_ZN18qdesigner_internal14SignaturePanelC1EP7QObjectP9QListViewP11QToolButtonS6_RK7QString(
    QObject *parent,
    QListView *listView,
    QToolButton *addButton,
    QToolButton *removeButton,
    const QString *newPrefix) {
  return new qdesigner_internal::SignaturePanel(
      parent,
      listView,
      addButton,
      removeButton,
      *newPrefix);
}

//  QStringList qdesigner_internal::SignaturePanel::fakeMethods() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal14SignaturePanel11fakeMethodsEv(
    const qdesigner_internal::SignaturePanel *self) {
  return new QList<QString>(self->fakeMethods());
}

//  void qdesigner_internal::SignaturePanel::setData(const
//      SignalSlotDialogData &d)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel7setDataERKNS_20SignalSlotDialogDataE(
    qdesigner_internal::SignaturePanel *self,
    const qdesigner_internal::SignalSlotDialogData *d) {
  self->setData(*d);
}

//  int qdesigner_internal::SignaturePanel::count(const QString &signature)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal14SignaturePanel5countERK7QString(
    const qdesigner_internal::SignaturePanel *self,
    const QString *signature) {
  return self->count(*signature);
}

//  void qdesigner_internal::SignaturePanel::checkSignature(const QString
//      &signature, bool *ok)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel14checkSignatureERK7QStringPb(
    qdesigner_internal::SignaturePanel *self,
    const QString *signature,
    bool *ok) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignaturePanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkSignature(const QString &,bool *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkSignature(const QString &,bool *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(signature)),
      const_cast<void *>(static_cast<const void *>(&ok)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::SignaturePanel::slotAdd()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel7slotAddEv(
    qdesigner_internal::SignaturePanel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignaturePanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotAdd()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotAdd()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::SignaturePanel::slotRemove()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel10slotRemoveEv(
    qdesigner_internal::SignaturePanel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignaturePanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotRemove()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotRemove()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::SignaturePanel::slotSelectionChanged(const
//      QItemSelection &a0, const QItemSelection &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel20slotSelectionChangedERK14QItemSelectionS3_(
    qdesigner_internal::SignaturePanel *self,
    const QItemSelection *a0,
    const QItemSelection *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::SignaturePanel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotSelectionChanged(const QItemSelection &,const QItemSelection &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotSelectionChanged(const QItemSelection &,const QItemSelection &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::SignaturePanel::closeEditor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14SignaturePanel11closeEditorEv(
    qdesigner_internal::SignaturePanel *self) {
  self->closeEditor();
}
