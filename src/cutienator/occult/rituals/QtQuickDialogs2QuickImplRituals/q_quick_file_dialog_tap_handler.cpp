//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelega
//  te_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QQuickFileDialogTapHandler' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qeventpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p_p.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qmimedata.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtQml/QQmlFile>
#include <QtQml/qqmlexpression.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
#include <QtQuick/private/qquicklistview_p.h>
#include <QtQuick/private/qquickitemview_p_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquicksidebar_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquicksidebar_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from QtQuickDialogs2QuickImpl__QQuickFileDialogTapHandler.cpp, line 1, as moc:QQuickFileDialogTapHandler
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN26QQuickFileDialogTapHandlerE_t {};
} // unnamed namespace

template <> constexpr inline auto QQuickFileDialogTapHandler::qt_create_metaobjectdata<qt_meta_tag_ZN26QQuickFileDialogTapHandlerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQuickFileDialogTapHandler"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QQuickFileDialogTapHandler, qt_meta_tag_ZN26QQuickFileDialogTapHandlerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QQuickFileDialogTapHandler::staticMetaObject = { {
    QMetaObject::SuperData::link<QQuickTapHandler::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QQuickFileDialogTapHandlerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QQuickFileDialogTapHandlerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN26QQuickFileDialogTapHandlerE_t>.metaTypes,
    nullptr
} };

void QQuickFileDialogTapHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQuickFileDialogTapHandler *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QQuickFileDialogTapHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQuickFileDialogTapHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN26QQuickFileDialogTapHandlerE_t>.strings))
        return static_cast<void*>(this);
    return QQuickTapHandler::qt_metacast(_clname);
}

int QQuickFileDialogTapHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QQuickTapHandler::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 426, as _ZN26QQuickFileDialogTapHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint
inline bool QQuickFileDialogTapHandler::wantsEventPoint(const QPointerEvent *event, const QEventPoint &point)
{
    if (!QQuickTapHandler::wantsEventPoint(event, point) || event->type() == QEvent::Type::Wheel)
        return false;

    // we only want the event point if the delegate contains a directory and not a file
    auto *fileDialogDelegate = qobject_cast<QQuickFileDialogDelegate *>(parent());
    QFileInfo info(fileDialogDelegate->file().toLocalFile());
    if (info.isDir())
        return true;

    return false;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 351, as _ZN26QQuickFileDialogTapHandler16handleEventPointEP13QPointerEventR11QEventPoint
inline void QQuickFileDialogTapHandler::handleEventPoint(QPointerEvent *event, QEventPoint &point)
{
    QQuickTapHandler::handleEventPoint(event, point);

    auto *fileDialogDelegate = qobject_cast<QQuickFileDialogDelegate *>(parent());
    auto *fileDialogImpl = getFileDialogImpl();
    if (Q_UNLIKELY(!fileDialogImpl))
        return;
    auto *fileDialogImplPrivate = QQuickFileDialogImplPrivate::get(fileDialogImpl);
    QQuickFileDialogImplAttached *attached = fileDialogImplPrivate->attachedOrWarn();
    if (Q_UNLIKELY(!attached || !attached->sideBar()))
        return;

    if (m_state == DraggingFinished)
        resetDragData();

    if (point.state() == QEventPoint::Pressed) {
        resetDragData();
        // Activate the passive grab to get further move updates
        setPassiveGrab(event, point, true);
    } else if (point.state() == QEventPoint::Released) {
        resetDragData();
    } else if (point.state() == QEventPoint::Updated && m_longPressed) {
        // Check to see that the movement can be considered as dragging
        const qreal distX = point.position().x() - point.pressPosition().x();
        const qreal distY = point.position().y() - point.pressPosition().y();
        // consider the squared distance to be optimal
        const qreal dragDistSq = distX * distX + distY * distY;
        if (dragDistSq > qPow(qApp->styleHints()->startDragDistance(), 2)) {
            switch (m_state) {
            case Tracking: {
                // set the drag
                if (m_drag.isNull())
                    m_drag = new QDrag(fileDialogDelegate);
                // Set the drop area
                if (m_dropArea.isNull()) {
                    auto *sideBar = attached->sideBar();
                    m_dropArea = new QQuickDropArea(sideBar);
                    m_dropArea->setSize(sideBar->size());
                    connect(m_dropArea, &QQuickDropArea::positionChanged, this,
                            &QQuickFileDialogTapHandler::handleDrag);
                    connect(m_dropArea, &QQuickDropArea::dropped, this,
                            &QQuickFileDialogTapHandler::handleDrop);
                    connect(m_dropArea, &QQuickDropArea::containsDragChanged, this,
                            &QQuickFileDialogTapHandler::handleContainsDragChanged);
                }

                m_sourceUrl = fileDialogDelegate->file();
                // set up the grab
                grabFolder();
                m_state = DraggingStarted;
            } break;

            case DraggingStarted: {
                if (m_drag && m_drag->mimeData()) {
                    if (auto *item = qobject_cast<QQuickItem *>(m_drag->source())) {
                        Q_UNUSED(item);
                        m_state = Dragging;
                        // start the drag
                        m_drag->exec();
                        // If the state still remains dragging, then the drop happened outside
                        // the drop area
                        if (m_state == Dragging)
                            resetDragData();
                    }
                }
            } break;

            default:
                break;
            }
        }
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 190, as _ZN26QQuickFileDialogTapHandlerC1EP10QQuickItem
inline QQuickFileDialogTapHandler::QQuickFileDialogTapHandler(QQuickItem *parent)
    : QQuickTapHandler(parent)
{
    // Set a grab permission that stops the flickable from stealing the drag.
    setGrabPermissions(QQuickPointerHandler::CanTakeOverFromAnything);

    // The drag threshold is used by the handler to know when to start a drag.
    // We handle the drag inpendently, so set the threshold to a big number.
    // This will guarantee that QQuickTapHandler::wantsEventPoint always returns
    // true.
    setDragThreshold(1000);
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 203, as _ZNK26QQuickFileDialogTapHandler17getFileDialogImplEv
inline QQuickFileDialogImpl *QQuickFileDialogTapHandler::getFileDialogImpl() const
{
    auto *delegate = qobject_cast<QQuickFileDialogDelegate*>(parent());
    auto *delegatePrivate = QQuickFileDialogDelegatePrivate::get(delegate);
    return delegatePrivate->fileDialog;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 210, as _ZN26QQuickFileDialogTapHandler10grabFolderEv
inline void QQuickFileDialogTapHandler::grabFolder()
{
    if (m_drag.isNull())
        return;

    QQuickPalette *palette = [this]() -> QQuickPalette* {
        auto *delegate = qobject_cast<QQuickFileDialogDelegate*>(parent());
        if (delegate) {
            QQuickDialog *dlg = delegate->dialog();
            if (dlg) {
                QQuickDialogPrivate *priv = QQuickDialogPrivate::get(dlg);
                if (priv)
                    return priv->palette();
            }
        }
        return nullptr;
    }();

    // TODO: use proper @Nx scaling
    const auto src = ":/qt-project.org/imports/QtQuick/Dialogs/quickimpl/images/sidebar-folder.png"_L1;
    QImage img = QImage(src).convertToFormat(QImage::Format_ARGB32);

    if (!img.isNull() && palette) {
        const QColor iconColor = palette->buttonText();
        if (iconColor.alpha() > 0) {
            // similar to what QQuickIconImage does
            QPainter painter(&img);
            painter.setCompositionMode(QPainter::CompositionMode_SourceIn);
            painter.fillRect(img.rect(), iconColor);
        }
    }

    QPixmap pixmap = QPixmap::fromImage(std::move(img));
    auto *mimeData = new QMimeData();
    mimeData->setImageData(pixmap);
    m_drag->setMimeData(mimeData);
    m_drag->setPixmap(pixmap);
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 249, as _ZNK26QQuickFileDialogTapHandler19getFolderUrlAtPressEv
inline QUrl QQuickFileDialogTapHandler::getFolderUrlAtPress() const
{
    auto *delegate = qobject_cast<QQuickFileDialogDelegate *>(parent());
    return QUrl{delegate->file().toLocalFile()};
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 255, as _ZN26QQuickFileDialogTapHandler10handleDragEP15QQuickDragEvent
inline void QQuickFileDialogTapHandler::handleDrag(QQuickDragEvent *event)
{
    if (m_state == Dragging) {
        auto *fileDialogImpl = getFileDialogImpl();
        auto *attached = QQuickFileDialogImplPrivate::get(fileDialogImpl)->attachedOrWarn();
        if (Q_LIKELY(attached)) {
            auto *sideBar = attached->sideBar();
            if (Q_LIKELY(sideBar)) {
                auto *sideBarPrivate = QQuickSideBarPrivate::get(sideBar);
                const auto pos = QPoint(event->x(), event->y());
                sideBarPrivate->setShowAddFavoriteDelegate(sideBar->contains(pos));
                if (sideBarPrivate->showAddFavoriteDelegate()) {
                    const QList<QQuickItem *> items = sideBar->contentChildren().toList<QList<QQuickItem *>>();
                    // iterate through the children until we have counted all the folder paths. The next button will
                    // be the addFavoriteDelegate
                    const int addFavoritePos = sideBar->effectiveFolderPaths().size();
                    int currentPos = 0;
                    for (int i = 0; i < items.length(); i++) {
                        if (auto *button = qobject_cast<QQuickAbstractButton *>(items.at(i))) {
                            if (currentPos == addFavoritePos) {
                                // check if the pointer position is within the add favorite button
                                const QRectF bBox = button->mapRectToItem(sideBar, button->boundingRect());
                                sideBarPrivate->setAddFavoriteDelegateHovered(bBox.contains(pos));
                                break;
                            } else {
                                currentPos++;
                            }
                        }
                    }
                }
            }
        }
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 290, as _ZN26QQuickFileDialogTapHandler10handleDropEP15QQuickDragEvent
inline void QQuickFileDialogTapHandler::handleDrop(QQuickDragEvent *event)
{
    Q_UNUSED(event);
    if (m_state == Dragging) {
        if (!m_sourceUrl.isEmpty()) {
            auto *fileDialogImpl = getFileDialogImpl();
            auto *attached = QQuickFileDialogImplPrivate::get(fileDialogImpl)->attachedOrWarn();
            if (Q_LIKELY(attached)) {
                auto *sideBar = attached->sideBar();
                if (Q_LIKELY(sideBar)) {
                    auto *sideBarPrivate = QQuickSideBarPrivate::get(sideBar);
                    // this cannot be handled in handleDrag because handleDrag is connected to the drop
                    // area, and so won't run when the cursor is outside of it
                    if (sideBarPrivate->addFavoriteDelegateHovered())
                        sideBarPrivate->addFavorite(m_sourceUrl);
                    sideBarPrivate->setShowAddFavoriteDelegate(false);
                }
            }
        }
        m_state = DraggingFinished;
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 313, as _ZN26QQuickFileDialogTapHandler25handleContainsDragChangedEv
inline void QQuickFileDialogTapHandler::handleContainsDragChanged()
{
    if (m_state == Dragging) {
        auto *fileDialogImpl = getFileDialogImpl();
        auto *attached = QQuickFileDialogImplPrivate::get(fileDialogImpl)->attachedOrWarn();
        if (Q_LIKELY(attached)) {
            auto *sideBar = attached->sideBar();
            if (Q_LIKELY(sideBar && m_dropArea)) {
                auto *sideBarPrivate = QQuickSideBarPrivate::get(sideBar);
                if (m_dropArea->containsDrag()) {
                    sideBarPrivate->setShowAddFavoriteDelegate(true);
                } else {
                    sideBarPrivate->setShowAddFavoriteDelegate(false);
                    sideBarPrivate->setAddFavoriteDelegateHovered(false);
                }
            }
        }
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogdelegate.cpp, line 333, as _ZN26QQuickFileDialogTapHandler13resetDragDataEv
inline void QQuickFileDialogTapHandler::resetDragData()
{
    if (m_state != Listening) {
        m_state = Listening;
        m_sourceUrl = QUrl();
        if (!m_drag.isNull()) {
            m_drag->disconnect();
            delete m_drag;
        }
        if (!m_dropArea.isNull()) {
            m_dropArea->disconnect();
            delete m_dropArea;
        }

        m_longPressed = false;
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickFileDialogTapHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFileDialogTapHandler : QQuickFileDialogTapHandler {
  using QQuickFileDialogTapHandler::wantsEventPoint;
};

//  const QMetaObject *QQuickFileDialogTapHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickFileDialogTapHandler10metaObjectEv(
    const QQuickFileDialogTapHandler *self) {
  return self->metaObject();
}

//  void *QQuickFileDialogTapHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQuickFileDialogTapHandler11qt_metacastEPKc(
    QQuickFileDialogTapHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFileDialogTapHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQuickFileDialogTapHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFileDialogTapHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFileDialogTapHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuickFileDialogTapHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFileDialogTapHandler::tr(s, c, n));
}

//  QQuickFileDialogTapHandler::QQuickFileDialogTapHandler(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickFileDialogTapHandler *ritual_ZN26QQuickFileDialogTapHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickFileDialogTapHandler(parent);
}

//  State QQuickFileDialogTapHandler::state()
extern "C" Q_DECL_EXPORT
QQuickFileDialogTapHandler::State ritual_ZN26QQuickFileDialogTapHandler5stateEv(
    QQuickFileDialogTapHandler *self) {
  return self->state();
}

//  QQuickFileDialogImpl *QQuickFileDialogTapHandler::getFileDialogImpl()
//      const
extern "C" Q_DECL_EXPORT
QQuickFileDialogImpl *ritual_ZNK26QQuickFileDialogTapHandler17getFileDialogImplEv(
    const QQuickFileDialogTapHandler *self) {
  return self->getFileDialogImpl();
}

//  void QQuickFileDialogTapHandler::grabFolder()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickFileDialogTapHandler10grabFolderEv(
    QQuickFileDialogTapHandler *self) {
  self->grabFolder();
}

//  QUrl QQuickFileDialogTapHandler::getFolderUrlAtPress() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK26QQuickFileDialogTapHandler19getFolderUrlAtPressEv(
    const QQuickFileDialogTapHandler *self) {
  return new QUrl(self->getFolderUrlAtPress());
}

//  void QQuickFileDialogTapHandler::handleDrag(QQuickDragEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickFileDialogTapHandler10handleDragEP15QQuickDragEvent(
    QQuickFileDialogTapHandler *self,
    QQuickDragEvent *event) {
  self->handleDrag(event);
}

//  void QQuickFileDialogTapHandler::handleDrop(QQuickDragEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickFileDialogTapHandler10handleDropEP15QQuickDragEvent(
    QQuickFileDialogTapHandler *self,
    QQuickDragEvent *event) {
  self->handleDrop(event);
}

//  void QQuickFileDialogTapHandler::handleContainsDragChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickFileDialogTapHandler25handleContainsDragChangedEv(
    QQuickFileDialogTapHandler *self) {
  self->handleContainsDragChanged();
}

//  void QQuickFileDialogTapHandler::handleEventPoint(QPointerEvent *event,
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickFileDialogTapHandler16handleEventPointEP13QPointerEventR11QEventPoint(
    QQuickFileDialogTapHandler *self,
    QPointerEvent *event,
    QEventPoint *point) {
  self->handleEventPoint(event, *point);
}

//  bool QQuickFileDialogTapHandler::wantsEventPoint(const QPointerEvent
//      *event, const QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickFileDialogTapHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickFileDialogTapHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return self->wantsEventPoint(event, *point);
}

//  void QQuickFileDialogTapHandler::resetDragData()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickFileDialogTapHandler13resetDragDataEv(
    QQuickFileDialogTapHandler *self) {
  self->resetDragData();
}

//  bool QQuickFileDialogTapHandler::wantsEventPoint(const QPointerEvent
//      *event, const QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QQuickFileDialogTapHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickFileDialogTapHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return static_cast<OwnQQuickFileDialogTapHandler *>(self)->OwnQQuickFileDialogTapHandler::wantsEventPoint(
      event,
      *point);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
