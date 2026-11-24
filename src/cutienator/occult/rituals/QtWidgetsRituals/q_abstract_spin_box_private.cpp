//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractspinbox_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(spinbox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qabstractspinbox.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractspinbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h>
#ifdef Q_OS_WASM
# include <private/qstdweb_p.h>
#endif
#include <private/qabstractspinbox_p.h>
#include <private/qapplication_p.h>
#if QT_CONFIG(datetimeparser)
#include <private/qdatetimeparser_p.h>
#endif
#include <private/qlineedit_p.h>
#include <qabstractspinbox.h>
#include <qapplication.h>
#include <qstylehints.h>
#include <qclipboard.h>
#include <qdatetime.h>
#include <qevent.h>
#include <qloggingcategory.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#include <qstylepainter.h>
#if QT_CONFIG(accessibility)
# include <qaccessible.h>
#endif
#include <QtCore/qpointer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1738, as _ZN23QAbstractSpinBoxPrivate10updateEditEv
inline void QAbstractSpinBoxPrivate::updateEdit()
{
    Q_Q(QAbstractSpinBox);
    if (type == QMetaType::UnknownType)
        return;
    const QString newText = specialValue() ? specialValueText : prefix + textFromValue(value) + suffix;
    if (newText == edit->displayText() || cleared)
        return;

    const bool empty = edit->text().isEmpty();
    int cursor = edit->cursorPosition();
    int selsize = edit->selectedText().size();
    const QSignalBlocker blocker(edit);
    edit->setText(newText);

    if (!specialValue()) {
        cursor = qBound(prefix.size(), cursor, edit->displayText().size() - suffix.size());

        if (selsize > 0) {
            edit->setSelection(cursor, selsize);
        } else {
            edit->setCursorPosition(empty ? prefix.size() : cursor);
        }
    }
    q->update();
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1466, as _ZN23QAbstractSpinBoxPrivate11emitSignalsE10EmitPolicyRK8QVariant
inline void QAbstractSpinBoxPrivate::emitSignals(EmitPolicy, const QVariant &)
{
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1397, as _ZN23QAbstractSpinBoxPrivate15newHoverControlERK6QPoint
inline QStyle::SubControl QAbstractSpinBoxPrivate::newHoverControl(const QPoint &pos)
{
    Q_Q(QAbstractSpinBox);

    QStyleOptionSpinBox opt;
    q->initStyleOption(&opt);
    opt.subControls = QStyle::SC_All;
    hoverControl = q->style()->hitTestComplexControl(QStyle::CC_SpinBox, &opt, pos, q);
    hoverRect = q->style()->subControlRect(QStyle::CC_SpinBox, &opt, hoverControl, q);
    return hoverControl;
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1442, as _ZN23QAbstractSpinBoxPrivate23updateEditFieldGeometryEv
inline void QAbstractSpinBoxPrivate::updateEditFieldGeometry()
{
    Q_Q(QAbstractSpinBox);
    QStyleOptionSpinBox opt;
    q->initStyleOption(&opt);
    opt.subControls = QStyle::SC_SpinBoxEditField;
    edit->setGeometry(q->style()->subControlRect(QStyle::CC_SpinBox, &opt,
                                                 QStyle::SC_SpinBoxEditField, q));
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1507, as _ZN23QAbstractSpinBoxPrivate27editorCursorPositionChangedEii
inline void QAbstractSpinBoxPrivate::editorCursorPositionChanged(int oldpos, int newpos)
{
    if (!edit->hasSelectedText() && !ignoreCursorPositionChanged && !specialValue()) {
        ignoreCursorPositionChanged = true;

        bool allowSelection = true;
        int pos = -1;
        if (newpos < prefix.size() && newpos != 0) {
            if (oldpos == 0) {
                allowSelection = false;
                pos = prefix.size();
            } else {
                pos = oldpos;
            }
        } else if (newpos > edit->text().size() - suffix.size()
                   && newpos != edit->text().size()) {
            if (oldpos == edit->text().size()) {
                pos = edit->text().size() - suffix.size();
                allowSelection = false;
            } else {
                pos = edit->text().size();
            }
        }
        if (pos != -1) {
            const int selSize = edit->selectionStart() >= 0 && allowSelection
                                  ? (edit->selectedText().size()
                                     * (newpos < pos ? -1 : 1)) - newpos + pos
                                  : 0;

            const QSignalBlocker blocker(edit);
            if (selSize != 0) {
                edit->setSelection(pos - selSize, selSize);
            } else {
                edit->setCursorPosition(pos);
            }
        }
        ignoreCursorPositionChanged = false;
    }
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1771, as _ZN23QAbstractSpinBoxPrivate8setRangeERK8QVariantS2_
inline void QAbstractSpinBoxPrivate::setRange(const QVariant &min, const QVariant &max)
{
    Q_Q(QAbstractSpinBox);

    clearCache();
    minimum = min;
    maximum = (variantCompare(min, max) < 0 ? max : min);
    cachedSizeHint = QSize();
    cachedMinimumSizeHint = QSize(); // minimumSizeHint cares about min/max

    reset();
    if (!(bound(value) == value)) {
        setValue(bound(value), EmitIfChanged);
    } else if (value == minimum && !specialValueText.isEmpty()) {
        updateEdit();
    }

    q->updateGeometry();
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1882, as _ZNK23QAbstractSpinBoxPrivate10clearCacheEv
inline void QAbstractSpinBoxPrivate::clearCache() const
{
    cachedText.clear();
    cachedValue.clear();
    cachedState = QValidator::Acceptable;
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1727, as _ZNK23QAbstractSpinBoxPrivate10roundValueERK8QVariant
inline QVariant QAbstractSpinBoxPrivate::roundValue(const QVariant &val) const
{
    return val;
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1819, as _ZNK23QAbstractSpinBoxPrivate13textFromValueERK8QVariant
inline QString QAbstractSpinBoxPrivate::textFromValue(const QVariant &) const
{
    return QString();
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1835, as _ZNK23QAbstractSpinBoxPrivate13valueFromTextERK7QString
inline QVariant QAbstractSpinBoxPrivate::valueFromText(const QString &) const
{
    return QVariant();
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1797, as _ZNK23QAbstractSpinBoxPrivate14getZeroVariantEv
inline QVariant QAbstractSpinBoxPrivate::getZeroVariant() const
{
    QVariant ret;
    switch (type) {
    case QMetaType::Int: ret = QVariant(0); break;
    case QMetaType::Double: ret = QVariant(0.0); break;
    default: break;
    }
    return ret;
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1889, as _ZNK23QAbstractSpinBoxPrivate28calculateAdaptiveDecimalStepEi
inline QVariant QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(int steps) const
{
    Q_UNUSED(steps);
    return singleStep;
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1672, as _ZNK23QAbstractSpinBoxPrivate5boundERK8QVariantS2_i
inline QVariant QAbstractSpinBoxPrivate::bound(const QVariant &val, const QVariant &old, int steps) const
{
    QVariant v = val;
    if (!wrapping || steps == 0 || old.isNull()) {
        if (variantCompare(v, minimum) < 0) {
            v = wrapping ? maximum : minimum;
        }
        if (variantCompare(v, maximum) > 0) {
            v = wrapping ? minimum : maximum;
        }
    } else {
        const bool wasMin = old == minimum;
        const bool wasMax = old == maximum;
        const int oldcmp = variantCompare(v, old);
        const int maxcmp = variantCompare(v, maximum);
        const int mincmp = variantCompare(v, minimum);
        const bool wrapped = (oldcmp > 0 && steps < 0) || (oldcmp < 0 && steps > 0);
        if (maxcmp > 0) {
            v = ((wasMax && !wrapped && steps > 0) || (steps < 0 && !wasMin && wrapped))
                ? minimum : maximum;
        } else if (wrapped && (maxcmp > 0 || mincmp < 0)) {
            v = ((wasMax && steps > 0) || (!wasMin && steps < 0)) ? minimum : maximum;
        } else if (mincmp < 0) {
            v = (!wasMax && !wasMin ? minimum : maximum);
        }
    }

    return v;
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1369, as _ZN23QAbstractSpinBoxPrivateD1Ev
inline QAbstractSpinBoxPrivate::~QAbstractSpinBoxPrivate()
{
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1582, as _ZN23QAbstractSpinBoxPrivate5resetEv
inline void QAbstractSpinBoxPrivate::reset()
{
    Q_Q(QAbstractSpinBox);

    buttonState = None;
    if (q) {
        spinClickTimer.stop();
        spinClickThresholdTimer.stop();
        acceleration = 0;
        q->update();
    }
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1414, as _ZNK23QAbstractSpinBoxPrivate8strippedERK7QStringPi
inline QString QAbstractSpinBoxPrivate::stripped(const QString &t, int *pos) const
{
    QStringView text(t);
    if (specialValueText.size() == 0 || text != specialValueText) {
        int from = 0;
        int size = text.size();
        bool changed = false;
        if (prefix.size() && text.startsWith(prefix)) {
            from += prefix.size();
            size -= from;
            changed = true;
        }
        if (suffix.size() && text.endsWith(suffix)) {
            size -= suffix.size();
            changed = true;
        }
        if (changed)
            text = text.mid(from, size);
    }

    const int s = text.size();
    text = text.trimmed();
    if (pos)
        (*pos) -= (s - text.size());
    return text.toString();

}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1456, as _ZNK23QAbstractSpinBoxPrivate12specialValueEv
inline bool QAbstractSpinBoxPrivate::specialValue() const
{
    return (value == minimum && !specialValueText.isEmpty());
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1709, as _ZN23QAbstractSpinBoxPrivate8setValueERK8QVariant10EmitPolicyb
inline void QAbstractSpinBoxPrivate::setValue(const QVariant &val, EmitPolicy ep,
                                       bool doUpdate)
{
    Q_Q(QAbstractSpinBox);
    const QVariant old = value;
    value = bound(val);
    pendingEmit = false;
    cleared = false;
    if (doUpdate) {
        updateEdit();
    }
    q->update();

    if (ep == AlwaysEmit || (ep == EmitIfChanged && old != value)) {
        emitSignals(ep, old);
    }
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1477, as _ZN23QAbstractSpinBoxPrivate17editorTextChangedERK7QString
inline void QAbstractSpinBoxPrivate::editorTextChanged(const QString &t)
{
    Q_Q(QAbstractSpinBox);

    if (keyboardTracking) {
        QString tmp = t;
        int pos = edit->cursorPosition();
        QValidator::State state = q->validate(tmp, pos);
        if (state == QValidator::Acceptable) {
            const QVariant v = valueFromText(tmp);
            setValue(v, EmitIfChanged, tmp != t);
            pendingEmit = false;
        } else {
            pendingEmit = true;
        }
    } else {
        pendingEmit = true;
    }
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1378, as _ZN23QAbstractSpinBoxPrivate18updateHoverControlERK6QPoint
inline bool QAbstractSpinBoxPrivate::updateHoverControl(const QPoint &pos)
{
    Q_Q(QAbstractSpinBox);
    QRect lastHoverRect = hoverRect;
    QStyle::SubControl lastHoverControl = hoverControl;
    bool doesHover = q->testAttribute(Qt::WA_Hover);
    if (lastHoverControl != newHoverControl(pos) && doesHover) {
        q->update(lastHoverRect);
        q->update(hoverRect);
        return true;
    }
    return !doesHover;
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 2080, as _ZN23QAbstractSpinBoxPrivate14variantCompareERK8QVariantS2_
inline int QAbstractSpinBoxPrivate::variantCompare(const QVariant &arg1, const QVariant &arg2)
{
    switch (arg2.userType()) {
    case QMetaType::QDate:
        Q_ASSERT_X(arg1.userType() == QMetaType::QDate, "QAbstractSpinBoxPrivate::variantCompare",
                   qPrintable(QString::fromLatin1("Internal error 1 (%1)").
                              arg(QString::fromLatin1(arg1.typeName()))));
        if (arg1.toDate() == arg2.toDate()) {
            return 0;
        } else if (arg1.toDate() < arg2.toDate()) {
            return -1;
        } else {
            return 1;
        }
    case QMetaType::QTime:
        Q_ASSERT_X(arg1.userType() == QMetaType::QTime, "QAbstractSpinBoxPrivate::variantCompare",
                   qPrintable(QString::fromLatin1("Internal error 2 (%1)").
                              arg(QString::fromLatin1(arg1.typeName()))));
        if (arg1.toTime() == arg2.toTime()) {
            return 0;
        } else if (arg1.toTime() < arg2.toTime()) {
            return -1;
        } else {
            return 1;
        }


    case QMetaType::QDateTime:
        if (arg1.toDateTime() == arg2.toDateTime()) {
            return 0;
        } else if (arg1.toDateTime() < arg2.toDateTime()) {
            return -1;
        } else {
            return 1;
        }
    case QMetaType::Int:
        if (arg1.toInt() == arg2.toInt()) {
            return 0;
        } else if (arg1.toInt() < arg2.toInt()) {
            return -1;
        } else {
            return 1;
        }
    case QMetaType::Double:
        if (arg1.toDouble() == arg2.toDouble()) {
            return 0;
        } else if (arg1.toDouble() < arg2.toDouble()) {
            return -1;
        } else {
            return 1;
        }
    case QMetaType::UnknownType:
        if (arg2.userType() == QMetaType::UnknownType)
            return 0;
        Q_FALLTHROUGH();
    default:
        Q_ASSERT_X(0, "QAbstractSpinBoxPrivate::variantCompare",
                   qPrintable(QString::fromLatin1("Internal error 3 (%1 %2)").
                              arg(QString::fromLatin1(arg1.typeName()),
                                  QString::fromLatin1(arg2.typeName()))));
    }
    return -2;
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 2144, as _ZN23QAbstractSpinBoxPrivate12variantBoundERK8QVariantS2_S2_
inline QVariant QAbstractSpinBoxPrivate::variantBound(const QVariant &min,
                                               const QVariant &value,
                                               const QVariant &max)
{
    Q_ASSERT(variantCompare(min, max) <= 0);
    if (variantCompare(min, value) < 0) {
        const int compMax = variantCompare(value, max);
        return (compMax < 0 ? value : max);
    } else {
        return min;
    }
}
//  -----------------------------------------------------------------------

//  A QAbstractSpinBoxPrivate that Python can take functions over in. Every QAbstractSpinBoxPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAbstractSpinBoxPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxPrivateCall1)(const void *, const QVariant *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAbstractSpinBoxPrivateCall2)(const void *, const QVariant *, const QVariant *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAbstractSpinBoxPrivateCall3)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxPrivateCall4)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxPrivateCall5)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxPrivateCall6)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQAbstractSpinBoxPrivateCall7)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAbstractSpinBoxPrivateCall8)(const void *, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxPrivateCall9)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAbstractSpinBoxPrivateCall10)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxPrivateCall12)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAbstractSpinBoxPrivateCall13)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
typedef void (*CuteQAbstractSpinBoxPrivateCall14)(const void *, bool, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall15)(const void *, int, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall16)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall17)(const void *, int *);
typedef void * (*CuteQAbstractSpinBoxPrivateCall18)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQAbstractSpinBoxPrivateCall19)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQAbstractSpinBoxPrivateCall20)(const void *, int *);
typedef int (*CuteQAbstractSpinBoxPrivateCall21)(const void *, int *);
typedef const QImage * (*CuteQAbstractSpinBoxPrivateCall22)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall23)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall24)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall25)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall26)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall27)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall28)(const void *, int *);
typedef void (*CuteQAbstractSpinBoxPrivateCall29)(const void *, int *);
typedef bool (*CuteQAbstractSpinBoxPrivateCall30)(const void *, int *);
typedef bool (*CuteQAbstractSpinBoxPrivateCall31)(const void *, int *);
class CuteQAbstractSpinBoxPrivate : public QAbstractSpinBoxPrivate {
public:
  using QAbstractSpinBoxPrivate::QAbstractSpinBoxPrivate;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate14getZeroVariantEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate8setRangeERK8QVariantS2_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate5boundERK8QVariantS2_i")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate10roundValueERK8QVariant")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate10updateEditEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate11emitSignalsE10EmitPolicyRK8QVariant")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate9interpretE10EmitPolicy")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate13textFromValueERK8QVariant")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate13valueFromTextERK7QString")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate27editorCursorPositionChangedEii")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate15newHoverControlERK6QPoint")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate10clearCacheEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate23updateEditFieldGeometryEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate28calculateAdaptiveDecimalStepEi")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[31] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBoxPrivate::getZeroVariant() const
  QVariant getZeroVariant() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall0 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall0>(taken[0]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBoxPrivate::getZeroVariant();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBoxPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall1 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall1>(taken[1]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QAbstractSpinBoxPrivate::setRange(min, max);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBoxPrivate::bound(const QVariant &val, const
  //      QVariant &old, int steps) const
  QVariant bound(
      const QVariant &val,
      const QVariant &old,
      int steps) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall2 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall2>(taken[2]);
      const QVariant * given = call(this, &val, &old, steps, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBoxPrivate::bound(val, old, steps);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBoxPrivate::roundValue(const QVariant &val)
  //      const
  QVariant roundValue(const QVariant &val) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall3 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall3>(taken[3]);
      const QVariant * given = call(this, &val, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBoxPrivate::roundValue(val);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBoxPrivate::updateEdit()
  void updateEdit() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall4 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSpinBoxPrivate::updateEdit();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBoxPrivate::emitSignals(EmitPolicy ep, const
  //      QVariant &old)
  void emitSignals(EmitPolicy ep, const QVariant &old) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall5 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall5>(taken[5]);
      call(this, static_cast<int>(ep), &old, &handled);
      if (handled) return;
    }
    QAbstractSpinBoxPrivate::emitSignals(ep, old);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBoxPrivate::interpret(EmitPolicy ep)
  void interpret(EmitPolicy ep) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall6 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall6>(taken[6]);
      call(this, static_cast<int>(ep), &handled);
      if (handled) return;
    }
    QAbstractSpinBoxPrivate::interpret(ep);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QString QAbstractSpinBoxPrivate::textFromValue(const QVariant &n)
  //      const
  QString textFromValue(const QVariant &n) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall7 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall7>(taken[7]);
      QString * given = call(this, &n, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAbstractSpinBoxPrivate::textFromValue(n);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBoxPrivate::valueFromText(const QString &input)
  //      const
  QVariant valueFromText(const QString &input) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall8 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall8>(taken[8]);
      const QVariant * given = call(this, &input, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBoxPrivate::valueFromText(input);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBoxPrivate::editorCursorPositionChanged(int oldpos,
  //      int newpos)
  void editorCursorPositionChanged(int oldpos, int newpos) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall9 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall9>(taken[9]);
      call(this, oldpos, newpos, &handled);
      if (handled) return;
    }
    QAbstractSpinBoxPrivate::editorCursorPositionChanged(oldpos, newpos);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QStyle::SubControl QAbstractSpinBoxPrivate::newHoverControl(const
  //      QPoint &pos)
  QStyle::SubControl newHoverControl(const QPoint &pos) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall10 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall10>(taken[10]);
      int given = call(this, &pos, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return QAbstractSpinBoxPrivate::newHoverControl(pos);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBoxPrivate::clearCache() const
  void clearCache() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall11 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSpinBoxPrivate::clearCache();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QAbstractSpinBoxPrivate::updateEditFieldGeometry()
  void updateEditFieldGeometry() override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall12 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSpinBoxPrivate::updateEditFieldGeometry();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(int
  //      steps) const
  QVariant calculateAdaptiveDecimalStep(int steps) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall13 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall13>(taken[13]);
      const QVariant * given = call(this, steps, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(steps);
  }
#endif  // QT_CONFIG(spinbox)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall14 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall15 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall15>(taken[15]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall16 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall17 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall18 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall19 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall19>(taken[19]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall20 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall20>(taken[20]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall21 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall22 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall22>(taken[22]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall23 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall24 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall25 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall26 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall27 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall28 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall29 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall30 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractSpinBoxPrivateCall31 call = reinterpret_cast<CuteQAbstractSpinBoxPrivateCall31>(taken[31]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QAbstractSpinBox *QAbstractSpinBoxPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractSpinBox *ritual_ZN23QAbstractSpinBoxPrivate6q_funcEv(
    QAbstractSpinBoxPrivate *self) {
  return self->q_func();
}

//  const QAbstractSpinBox *QAbstractSpinBoxPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractSpinBox *ritual_ZNK23QAbstractSpinBoxPrivate6q_funcEv(
    const QAbstractSpinBoxPrivate *self) {
  return self->q_func();
}

//  QAbstractSpinBoxPrivate::~QAbstractSpinBoxPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivateD1Ev(QAbstractSpinBoxPrivate *self) {
  delete self;
}

//  void QAbstractSpinBoxPrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate5resetEv(
    QAbstractSpinBoxPrivate *self) {
  self->reset();
}

//  QString QAbstractSpinBoxPrivate::stripped(const QString &text, int *pos)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QAbstractSpinBoxPrivate8strippedERK7QStringPi(
    const QAbstractSpinBoxPrivate *self,
    const QString *text,
    int *pos) {
  return new QString(self->stripped(*text, pos));
}

//  bool QAbstractSpinBoxPrivate::specialValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QAbstractSpinBoxPrivate12specialValueEv(
    const QAbstractSpinBoxPrivate *self) {
  return self->specialValue();
}

//  QVariant QAbstractSpinBoxPrivate::getZeroVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QAbstractSpinBoxPrivate14getZeroVariantEv(
    const QAbstractSpinBoxPrivate *self) {
  return new QVariant(self->getZeroVariant());
}

//  void QAbstractSpinBoxPrivate::setRange(const QVariant &min, const
//      QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate8setRangeERK8QVariantS2_(
    QAbstractSpinBoxPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  void QAbstractSpinBoxPrivate::setValue(const QVariant &val, EmitPolicy
//      ep, bool updateEdit)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate8setValueERK8QVariant10EmitPolicyb(
    QAbstractSpinBoxPrivate *self,
    const QVariant *val,
    EmitPolicy ep,
    bool updateEdit) {
  self->setValue(*val, ep, updateEdit);
}

//  QVariant QAbstractSpinBoxPrivate::bound(const QVariant &val, const
//      QVariant &old, int steps) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QAbstractSpinBoxPrivate5boundERK8QVariantS2_i(
    const QAbstractSpinBoxPrivate *self,
    const QVariant *val,
    const QVariant *old,
    int steps) {
  return new QVariant(self->bound(*val, *old, steps));
}

//  QVariant QAbstractSpinBoxPrivate::roundValue(const QVariant &val) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QAbstractSpinBoxPrivate10roundValueERK8QVariant(
    const QAbstractSpinBoxPrivate *self,
    const QVariant *val) {
  return new QVariant(self->roundValue(*val));
}

//  void QAbstractSpinBoxPrivate::updateEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate10updateEditEv(
    QAbstractSpinBoxPrivate *self) {
  self->updateEdit();
}

//  void QAbstractSpinBoxPrivate::emitSignals(EmitPolicy ep, const QVariant
//      &old)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate11emitSignalsE10EmitPolicyRK8QVariant(
    QAbstractSpinBoxPrivate *self,
    EmitPolicy ep,
    const QVariant *old) {
  self->emitSignals(ep, *old);
}

//  void QAbstractSpinBoxPrivate::interpret(EmitPolicy ep)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate9interpretE10EmitPolicy(
    QAbstractSpinBoxPrivate *self,
    EmitPolicy ep) {
  self->interpret(ep);
}

//  QString QAbstractSpinBoxPrivate::textFromValue(const QVariant &n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QAbstractSpinBoxPrivate13textFromValueERK8QVariant(
    const QAbstractSpinBoxPrivate *self,
    const QVariant *n) {
  return new QString(self->textFromValue(*n));
}

//  QVariant QAbstractSpinBoxPrivate::valueFromText(const QString &input)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QAbstractSpinBoxPrivate13valueFromTextERK7QString(
    const QAbstractSpinBoxPrivate *self,
    const QString *input) {
  return new QVariant(self->valueFromText(*input));
}

//  void QAbstractSpinBoxPrivate::editorTextChanged(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate17editorTextChangedERK7QString(
    QAbstractSpinBoxPrivate *self,
    const QString *a0) {
  self->editorTextChanged(*a0);
}

//  void QAbstractSpinBoxPrivate::editorCursorPositionChanged(int oldpos, int
//      newpos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate27editorCursorPositionChangedEii(
    QAbstractSpinBoxPrivate *self,
    int oldpos,
    int newpos) {
  self->editorCursorPositionChanged(oldpos, newpos);
}

//  QStyle::SubControl QAbstractSpinBoxPrivate::newHoverControl(const QPoint
//      &pos)
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZN23QAbstractSpinBoxPrivate15newHoverControlERK6QPoint(
    QAbstractSpinBoxPrivate *self,
    const QPoint *pos) {
  return self->newHoverControl(*pos);
}

//  bool QAbstractSpinBoxPrivate::updateHoverControl(const QPoint &pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QAbstractSpinBoxPrivate18updateHoverControlERK6QPoint(
    QAbstractSpinBoxPrivate *self,
    const QPoint *pos) {
  return self->updateHoverControl(*pos);
}

//  void QAbstractSpinBoxPrivate::clearCache() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QAbstractSpinBoxPrivate10clearCacheEv(
    const QAbstractSpinBoxPrivate *self) {
  self->clearCache();
}

//  void QAbstractSpinBoxPrivate::updateEditFieldGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractSpinBoxPrivate23updateEditFieldGeometryEv(
    QAbstractSpinBoxPrivate *self) {
  self->updateEditFieldGeometry();
}

//  int QAbstractSpinBoxPrivate::variantCompare(const QVariant &arg1, const
//      QVariant &arg2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QAbstractSpinBoxPrivate14variantCompareERK8QVariantS2_(
    const QVariant *arg1,
    const QVariant *arg2) {
  return QAbstractSpinBoxPrivate::variantCompare(*arg1, *arg2);
}

//  QVariant QAbstractSpinBoxPrivate::variantBound(const QVariant &min, const
//      QVariant &value, const QVariant &max)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN23QAbstractSpinBoxPrivate12variantBoundERK8QVariantS2_S2_(
    const QVariant *min,
    const QVariant *value,
    const QVariant *max) {
  return new QVariant(
      QAbstractSpinBoxPrivate::variantBound(
          *min,
          *value,
          *max));
}

//  QVariant QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(int steps)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QAbstractSpinBoxPrivate28calculateAdaptiveDecimalStepEi(
    const QAbstractSpinBoxPrivate *self,
    int steps) {
  return new QVariant(self->calculateAdaptiveDecimalStep(steps));
}

//  a Python function taken by a CuteQAbstractSpinBoxPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSpinBoxPrivate(
    QAbstractSpinBoxPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSpinBoxPrivate *>(self)->take(key, call);
}

//  QVariant QAbstractSpinBoxPrivate::getZeroVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QAbstractSpinBoxPrivate14getZeroVariantEv(
    const QAbstractSpinBoxPrivate *self) {
  return new QVariant(self->QAbstractSpinBoxPrivate::getZeroVariant());
}

//  void QAbstractSpinBoxPrivate::setRange(const QVariant &min, const
//      QVariant &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstractSpinBoxPrivate8setRangeERK8QVariantS2_(
    QAbstractSpinBoxPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->QAbstractSpinBoxPrivate::setRange(*min, *max);
}

//  QVariant QAbstractSpinBoxPrivate::bound(const QVariant &val, const
//      QVariant &old, int steps) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QAbstractSpinBoxPrivate5boundERK8QVariantS2_i(
    const QAbstractSpinBoxPrivate *self,
    const QVariant *val,
    const QVariant *old,
    int steps) {
  return new QVariant(
      self->QAbstractSpinBoxPrivate::bound(
          *val,
          *old,
          steps));
}

//  QVariant QAbstractSpinBoxPrivate::roundValue(const QVariant &val) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QAbstractSpinBoxPrivate10roundValueERK8QVariant(
    const QAbstractSpinBoxPrivate *self,
    const QVariant *val) {
  return new QVariant(self->QAbstractSpinBoxPrivate::roundValue(*val));
}

//  void QAbstractSpinBoxPrivate::updateEdit()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstractSpinBoxPrivate10updateEditEv(
    QAbstractSpinBoxPrivate *self) {
  self->QAbstractSpinBoxPrivate::updateEdit();
}

//  void QAbstractSpinBoxPrivate::emitSignals(EmitPolicy ep, const QVariant
//      &old)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstractSpinBoxPrivate11emitSignalsE10EmitPolicyRK8QVariant(
    QAbstractSpinBoxPrivate *self,
    EmitPolicy ep,
    const QVariant *old) {
  self->QAbstractSpinBoxPrivate::emitSignals(ep, *old);
}

//  QString QAbstractSpinBoxPrivate::textFromValue(const QVariant &n) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK23QAbstractSpinBoxPrivate13textFromValueERK8QVariant(
    const QAbstractSpinBoxPrivate *self,
    const QVariant *n) {
  return new QString(self->QAbstractSpinBoxPrivate::textFromValue(*n));
}

//  QVariant QAbstractSpinBoxPrivate::valueFromText(const QString &input)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QAbstractSpinBoxPrivate13valueFromTextERK7QString(
    const QAbstractSpinBoxPrivate *self,
    const QString *input) {
  return new QVariant(self->QAbstractSpinBoxPrivate::valueFromText(*input));
}

//  void QAbstractSpinBoxPrivate::editorCursorPositionChanged(int oldpos, int
//      newpos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstractSpinBoxPrivate27editorCursorPositionChangedEii(
    QAbstractSpinBoxPrivate *self,
    int oldpos,
    int newpos) {
  self->QAbstractSpinBoxPrivate::editorCursorPositionChanged(oldpos, newpos);
}

//  QStyle::SubControl QAbstractSpinBoxPrivate::newHoverControl(const QPoint
//      &pos)
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_own_ZN23QAbstractSpinBoxPrivate15newHoverControlERK6QPoint(
    QAbstractSpinBoxPrivate *self,
    const QPoint *pos) {
  return self->QAbstractSpinBoxPrivate::newHoverControl(*pos);
}

//  void QAbstractSpinBoxPrivate::clearCache() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK23QAbstractSpinBoxPrivate10clearCacheEv(
    const QAbstractSpinBoxPrivate *self) {
  self->QAbstractSpinBoxPrivate::clearCache();
}

//  void QAbstractSpinBoxPrivate::updateEditFieldGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QAbstractSpinBoxPrivate23updateEditFieldGeometryEv(
    QAbstractSpinBoxPrivate *self) {
  self->QAbstractSpinBoxPrivate::updateEditFieldGeometry();
}

//  QVariant QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(int steps)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QAbstractSpinBoxPrivate28calculateAdaptiveDecimalStepEi(
    const QAbstractSpinBoxPrivate *self,
    int steps) {
  return new QVariant(
      self->QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(
          steps));
}

#endif  // QT_CONFIG(spinbox)
