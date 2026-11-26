//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/qlayout_widget_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/private/layout_p.h>
#include <QtDesigner/private/layoutinfo_p.h>
#include <QtDesigner/private/invisible_widget_p.h>
#include <QtDesigner/private/qdesigner_widgetitem_p.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/propertysheet.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qgridlayout.h>
#include <QtWidgets/qformlayout.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtCore/qalgorithms.h>
#include <QtCore/qhash.h>
#include <QtCore/qmap.h>
#include <QtCore/qstack.h>
#include <QtCore/qset.h>
#include <utility>
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

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 457, as local:qlayout_widget.cpp:BoxLayoutHelper
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
class BoxLayoutHelper : public  LayoutHelper {
    public:
        BoxLayoutHelper(const Qt::Orientation orientation) : m_orientation(orientation) {}

        QRect itemInfo(QLayout *lt, int index) const override;
        void insertWidget(QLayout *lt, const QRect &info, QWidget *w) override;
        void removeWidget(QLayout *lt, QWidget *widget) override;
        void replaceWidget(QLayout *lt, QWidget *before, QWidget *after) override;

        void pushState(const QDesignerFormEditorInterface *, const QWidget *) override;
        void popState(const QDesignerFormEditorInterface *, QWidget *) override;

        bool canSimplify(const QDesignerFormEditorInterface *, const QWidget *, const QRect &) const override { return  false; }
        void simplify(const QDesignerFormEditorInterface *, QWidget *, const QRect &) override {}

        // Helper for restoring layout states
        using LayoutItemVector = QList<QLayoutItem *>;
        static LayoutItemVector disassembleLayout(QLayout *lt);
        static QLayoutItem *findItemOfWidget(const LayoutItemVector &lv, QWidget *w);

    private:
        using BoxLayoutState = QList<QWidget *>;

        static BoxLayoutState state(const QBoxLayout*lt);

        QStack<BoxLayoutState> m_states;
        const Qt::Orientation m_orientation;
    };
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 486, as local:qlayout_widget.cpp:BoxLayoutHelper::itemInfo
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QRect BoxLayoutHelper::itemInfo(QLayout * /*lt*/, int index) const
    {
        return m_orientation == Qt::Horizontal ?  QRect(index, 0, 1, 1) : QRect(0, index, 1, 1);
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 491, as local:qlayout_widget.cpp:BoxLayoutHelper::insertWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void BoxLayoutHelper::insertWidget(QLayout *lt, const QRect &info, QWidget *w)
    {
        QDesignerWidgetItemInstaller wii; // Make sure we use QDesignerWidgetItem.
        QBoxLayout *boxLayout = qobject_cast<QBoxLayout *>(lt);
        Q_ASSERT(boxLayout);
        boxLayout->insertWidget(m_orientation == Qt::Horizontal ? info.x() : info.y(), w);
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 499, as local:qlayout_widget.cpp:BoxLayoutHelper::removeWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void BoxLayoutHelper::removeWidget(QLayout *lt, QWidget *widget)
    {
        QBoxLayout *boxLayout = qobject_cast<QBoxLayout *>(lt);
        Q_ASSERT(boxLayout);
        boxLayout->removeWidget(widget);
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 506, as local:qlayout_widget.cpp:BoxLayoutHelper::replaceWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void BoxLayoutHelper::replaceWidget(QLayout *lt, QWidget *before, QWidget *after)
    {
        bool ok = false;
        QDesignerWidgetItemInstaller wii; // Make sure we use QDesignerWidgetItem.
        if (QBoxLayout *boxLayout = qobject_cast<QBoxLayout *>(lt)) {
            const int index = boxLayout->indexOf(before);
            if (index != -1) {
                const bool visible = before->isVisible();
                delete boxLayout->takeAt(index);
                if (visible)
                    before->hide();
                before->setParent(nullptr);
                boxLayout->insertWidget(index, after);
                ok = true;
            }
        }
        if (!ok)
            qWarning() << "BoxLayoutHelper::replaceWidget : Unable to replace " << before << " by " << after << " in " << lt;
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 526, as local:qlayout_widget.cpp:BoxLayoutHelper::state
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline BoxLayoutHelper::BoxLayoutState BoxLayoutHelper::state(const QBoxLayout*lt)
    {
        BoxLayoutState rc;
        if (const int count = lt->count()) {
            rc.reserve(count);
            for (int i = 0; i < count; i++)
                if (QWidget *w = lt->itemAt(i)->widget())
                    rc.push_back(w);
        }
        return rc;
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 538, as local:qlayout_widget.cpp:BoxLayoutHelper::pushState
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void BoxLayoutHelper::pushState(const QDesignerFormEditorInterface *core, const QWidget *w)
    {
        const QBoxLayout *boxLayout = qobject_cast<const QBoxLayout *>(LayoutInfo::managedLayout(core, w));
        Q_ASSERT(boxLayout);
        m_states.push(state(boxLayout));
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 545, as local:qlayout_widget.cpp:BoxLayoutHelper::findItemOfWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QLayoutItem *BoxLayoutHelper::findItemOfWidget(const LayoutItemVector &lv, QWidget *w)
    {
        for (auto *l : lv) {
            if (l->widget() == w)
                 return l;
        }
        return nullptr;
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 554, as local:qlayout_widget.cpp:BoxLayoutHelper::disassembleLayout
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline BoxLayoutHelper::LayoutItemVector BoxLayoutHelper::disassembleLayout(QLayout *lt)
    {
        // Take items
        const int count = lt->count();
        if (count == 0)
            return LayoutItemVector();
        LayoutItemVector rc;
        rc.reserve(count);
        for (int i = count - 1; i >= 0; i--)
            rc.push_back(lt->takeAt(i));
        return rc;
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 567, as local:qlayout_widget.cpp:BoxLayoutHelper::popState
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void BoxLayoutHelper::popState(const QDesignerFormEditorInterface *core, QWidget *w)
    {
        QBoxLayout *boxLayout = qobject_cast<QBoxLayout *>(LayoutInfo::managedLayout(core, w));
        Q_ASSERT(boxLayout);
        const BoxLayoutState savedState = m_states.pop();
        const BoxLayoutState currentState = state(boxLayout);
        // Check for equality/empty. Note that this will currently
        // always trigger as box layouts do not have a state apart from
        // the order and there is no layout order editor yet.
        if (savedState == state(boxLayout))
            return;

        Q_ASSERT(savedState.size() == currentState.size());
        // Take items and reassemble in saved order
        const LayoutItemVector items = disassembleLayout(boxLayout);
        for (auto *w : savedState) {
            QLayoutItem *item = findItemOfWidget(items, w);
            Q_ASSERT(item);
            boxLayout->addItem(item);
        }
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 432, as _ZN18qdesigner_internal12LayoutHelperD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline LayoutHelper::~LayoutHelper() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 430, as _ZN18qdesigner_internal12LayoutHelperC1Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline LayoutHelper::LayoutHelper() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 434, as _ZN18qdesigner_internal12LayoutHelper7indexOfEPK7QLayoutPK7QWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline int LayoutHelper::indexOf(const QLayout *lt, const QWidget *widget)
{
    if (!lt)
        return -1;

    const int itemCount = lt->count();
    for (int i = 0; i < itemCount; i++)
        if (lt->itemAt(i)->widget() == widget)
            return i;
    return -1;
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qlayout_widget.cpp, line 446, as _ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayoutPK7QWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QRect LayoutHelper::itemInfo(QLayout *lt, const QWidget *widget) const
{
    const int index = indexOf(lt, widget);
    if (index == -1) {
        qWarning() << "LayoutHelper::itemInfo: " << widget << " not in layout " << lt;
        return QRect(0, 0, 1, 1);
    }
    return itemInfo(lt, index);
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::LayoutHelper that Python can take functions over in. Every qdesigner_internal::LayoutHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRect * (*Cuteqdesigner_internal_LayoutHelperCall0)(const void *, QLayout *, int, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall1)(const void *, QLayout *, const QRect *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall2)(const void *, QLayout *, QWidget *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall3)(const void *, QLayout *, QWidget *, QWidget *, int *);
typedef bool (*Cuteqdesigner_internal_LayoutHelperCall4)(const void *, const QDesignerFormEditorInterface *, const QWidget *, const QRect *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall5)(const void *, const QDesignerFormEditorInterface *, QWidget *, const QRect *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall6)(const void *, const QDesignerFormEditorInterface *, const QWidget *, int *);
typedef void (*Cuteqdesigner_internal_LayoutHelperCall7)(const void *, const QDesignerFormEditorInterface *, QWidget *, int *);
class Cuteqdesigner_internal_LayoutHelper : public qdesigner_internal::LayoutHelper {
public:
  using qdesigner_internal::LayoutHelper::LayoutHelper;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayouti")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper12insertWidgetEP7QLayoutRK5QRectP7QWidget")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper12removeWidgetEP7QLayoutP7QWidget")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper13replaceWidgetEP7QLayoutP7QWidgetS4_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18qdesigner_internal12LayoutHelper11canSimplifyEPK28QDesignerFormEditorInterfacePK7QWidgetRK5QRect")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper8simplifyEPK28QDesignerFormEditorInterfaceP7QWidgetRK5QRect")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper9pushStateEPK28QDesignerFormEditorInterfacePK7QWidget")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18qdesigner_internal12LayoutHelper8popStateEPK28QDesignerFormEditorInterfaceP7QWidget")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt, int
  //      index) const
  QRect itemInfo(QLayout *lt, int index) const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall0 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall0>(taken[0]);
      const QRect * given = call(this, lt, index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void qdesigner_internal::LayoutHelper::insertWidget(QLayout *lt,
  //      const QRect &info, QWidget *w)
  void insertWidget(QLayout *lt, const QRect &info, QWidget *w) override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall1 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall1>(taken[1]);
      call(this, lt, &info, w, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::LayoutHelper::removeWidget(QLayout *lt,
  //      QWidget *widget)
  void removeWidget(QLayout *lt, QWidget *widget) override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall2 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall2>(taken[2]);
      call(this, lt, widget, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::LayoutHelper::replaceWidget(QLayout *lt,
  //      QWidget *before, QWidget *after)
  void replaceWidget(QLayout *lt, QWidget *before, QWidget *after) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall3 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall3>(taken[3]);
      call(this, lt, before, after, &handled);
      if (handled) return;
    }
  }

  //  bool qdesigner_internal::LayoutHelper::canSimplify(const
  //      QDesignerFormEditorInterface *core, const QWidget
  //      *widgetWithManagedLayout, const QRect &restrictionArea) const
  bool canSimplify(
      const QDesignerFormEditorInterface *core,
      const QWidget *widgetWithManagedLayout,
      const QRect &restrictionArea) const override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall4 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall4>(taken[4]);
      bool given = call(this, core, widgetWithManagedLayout, &restrictionArea, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void qdesigner_internal::LayoutHelper::simplify(const
  //      QDesignerFormEditorInterface *core, QWidget
  //      *widgetWithManagedLayout, const QRect &restrictionArea)
  void simplify(
      const QDesignerFormEditorInterface *core,
      QWidget *widgetWithManagedLayout,
      const QRect &restrictionArea) override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall5 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall5>(taken[5]);
      call(this, core, widgetWithManagedLayout, &restrictionArea, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::LayoutHelper::pushState(const
  //      QDesignerFormEditorInterface *core, const QWidget
  //      *widgetWithManagedLayout)
  void pushState(
      const QDesignerFormEditorInterface *core,
      const QWidget *widgetWithManagedLayout) override {
    if (taken[6]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall6 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall6>(taken[6]);
      call(this, core, widgetWithManagedLayout, &handled);
      if (handled) return;
    }
  }

  //  void qdesigner_internal::LayoutHelper::popState(const
  //      QDesignerFormEditorInterface *core, QWidget
  //      *widgetWithManagedLayout)
  void popState(
      const QDesignerFormEditorInterface *core,
      QWidget *widgetWithManagedLayout) override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_LayoutHelperCall7 call = reinterpret_cast<Cuteqdesigner_internal_LayoutHelperCall7>(taken[7]);
      call(this, core, widgetWithManagedLayout, &handled);
      if (handled) return;
    }
  }
};

//  qdesigner_internal::LayoutHelper::LayoutHelper()
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutHelper *ritual_ZN18qdesigner_internal12LayoutHelperC1Ev() {
  return new Cuteqdesigner_internal_LayoutHelper();
}

//  qdesigner_internal::LayoutHelper::~LayoutHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelperD1Ev(
    qdesigner_internal::LayoutHelper *self) {
  delete self;
}

//  int qdesigner_internal::LayoutHelper::indexOf(const QLayout *lt, const
//      QWidget *widget)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal12LayoutHelper7indexOfEPK7QLayoutPK7QWidget(
    const QLayout *lt,
    const QWidget *widget) {
  return qdesigner_internal::LayoutHelper::indexOf(lt, widget);
}

//  QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt, const
//      QWidget *widget) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayoutPK7QWidget(
    const qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    const QWidget *widget) {
  return new QRect(self->itemInfo(lt, widget));
}

//  QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt, int index)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayouti(
    const qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    int index) {
  return new QRect(self->itemInfo(lt, index));
}

//  void qdesigner_internal::LayoutHelper::insertWidget(QLayout *lt, const
//      QRect &info, QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper12insertWidgetEP7QLayoutRK5QRectP7QWidget(
    qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    const QRect *info,
    QWidget *w) {
  self->insertWidget(lt, *info, w);
}

//  void qdesigner_internal::LayoutHelper::removeWidget(QLayout *lt, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper12removeWidgetEP7QLayoutP7QWidget(
    qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    QWidget *widget) {
  self->removeWidget(lt, widget);
}

//  void qdesigner_internal::LayoutHelper::replaceWidget(QLayout *lt, QWidget
//      *before, QWidget *after)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper13replaceWidgetEP7QLayoutP7QWidgetS4_(
    qdesigner_internal::LayoutHelper *self,
    QLayout *lt,
    QWidget *before,
    QWidget *after) {
  self->replaceWidget(lt, before, after);
}

//  bool qdesigner_internal::LayoutHelper::canSimplify(const
//      QDesignerFormEditorInterface *core, const QWidget
//      *widgetWithManagedLayout, const QRect &restrictionArea) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal12LayoutHelper11canSimplifyEPK28QDesignerFormEditorInterfacePK7QWidgetRK5QRect(
    const qdesigner_internal::LayoutHelper *self,
    const QDesignerFormEditorInterface *core,
    const QWidget *widgetWithManagedLayout,
    const QRect *restrictionArea) {
  return self->canSimplify(core, widgetWithManagedLayout, *restrictionArea);
}

//  void qdesigner_internal::LayoutHelper::simplify(const
//      QDesignerFormEditorInterface *core, QWidget *widgetWithManagedLayout,
//      const QRect &restrictionArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper8simplifyEPK28QDesignerFormEditorInterfaceP7QWidgetRK5QRect(
    qdesigner_internal::LayoutHelper *self,
    const QDesignerFormEditorInterface *core,
    QWidget *widgetWithManagedLayout,
    const QRect *restrictionArea) {
  self->simplify(core, widgetWithManagedLayout, *restrictionArea);
}

//  void qdesigner_internal::LayoutHelper::pushState(const
//      QDesignerFormEditorInterface *core, const QWidget
//      *widgetWithManagedLayout)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper9pushStateEPK28QDesignerFormEditorInterfacePK7QWidget(
    qdesigner_internal::LayoutHelper *self,
    const QDesignerFormEditorInterface *core,
    const QWidget *widgetWithManagedLayout) {
  self->pushState(core, widgetWithManagedLayout);
}

//  void qdesigner_internal::LayoutHelper::popState(const
//      QDesignerFormEditorInterface *core, QWidget *widgetWithManagedLayout)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12LayoutHelper8popStateEPK28QDesignerFormEditorInterfaceP7QWidget(
    qdesigner_internal::LayoutHelper *self,
    const QDesignerFormEditorInterface *core,
    QWidget *widgetWithManagedLayout) {
  self->popState(core, widgetWithManagedLayout);
}

//  a Python function taken by a Cuteqdesigner_internal_LayoutHelper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_LayoutHelper(
    qdesigner_internal::LayoutHelper *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_LayoutHelper *>(self)->take(key, call);
}
