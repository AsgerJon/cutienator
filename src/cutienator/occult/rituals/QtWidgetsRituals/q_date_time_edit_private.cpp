//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdatetimeedit_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qdatetimeedit.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdatetimeedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qtimezone.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlocale.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdatetimeparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/qapplication_p.h>
#include <private/qdatetimeedit_p.h>
#include <qabstractspinbox.h>
#include <qapplication.h>
#include <qdatetimeedit.h>
#include <qdebug.h>
#include <qevent.h>
#include <qlineedit.h>
#include <private/qlineedit_p.h>
#include <qlocale.h>
#include <qpainter.h>
#include <qlayout.h>
#include <qset.h>
#include <qstyle.h>
#include <qstylepainter.h>
#include <algorithm>
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

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2626, as _ZN14QCalendarPopup12setDateRangeE5QDateS0_
inline void QCalendarPopup::setDateRange(QDate min, QDate max)
{
    QCalendarWidget *cw = verifyCalendarInstance();
    cw->setMinimumDate(min);
    cw->setMaximumDate(max);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2620, as _ZN14QCalendarPopup7setDateE5QDate
inline void QCalendarPopup::setDate(QDate date)
{
    oldDate = date;
    verifyCalendarInstance()->setSelectedDate(date);
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

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1358, as _ZN23QAbstractSpinBoxPrivateC2Ev
inline QAbstractSpinBoxPrivate::QAbstractSpinBoxPrivate()
    :  pendingEmit(false), readOnly(false), wrapping(false),
       ignoreCursorPositionChanged(false), frame(true), accelerate(false), keyboardTracking(true),
       cleared(false), ignoreUpdateEdit(false), showGroupSeparator(false)
{
}

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1369, as _ZN23QAbstractSpinBoxPrivateD2Ev
inline QAbstractSpinBoxPrivate::~QAbstractSpinBoxPrivate()
{
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1868, as _ZNK20QDateTimeEditPrivate20validateAndInterpretER7QStringRiRN10QValidator5StateEb
inline QDateTime QDateTimeEditPrivate::validateAndInterpret(QString &input, int &position,
                                                     QValidator::State &state, bool fixup) const
{
    if (input.isEmpty()) {
        if (sectionNodes.size() == 1 || !specialValueText.isEmpty()) {
            state = QValidator::Intermediate;
        } else {
            state = QValidator::Invalid;
        }
        return getZeroVariant().toDateTime();
    } else if (cachedText == input && !fixup) {
        state = cachedState;
        return cachedValue.toDateTime();
    } else if (!specialValueText.isEmpty()) {
        bool changeCase = false;
        const int max = qMin(specialValueText.size(), input.size());
        int i;
        for (i=0; i<max; ++i) {
            const QChar ic = input.at(i);
            const QChar sc = specialValueText.at(i);
            if (ic != sc) {
                if (sc.toLower() == ic.toLower()) {
                    changeCase = true;
                } else {
                    break;
                }
            }
        }
        if (i == max) {
            state = specialValueText.size() == input.size() ? QValidator::Acceptable : QValidator::Intermediate;
            if (changeCase) {
                input = specialValueText.left(max);
            }
            return minimum.toDateTime();
        }
    }

    StateNode tmp = parse(input, position, value.toDateTime(), fixup);
    // Take note of any corrections imposed during parsing:
    input = m_text;
    // TODO: if the format specifies time-zone, update timeZone to match the
    // parsed text; but we're in const context, so can't - QTBUG-118393.
    // Impose this widget's time system:
    tmp.value = tmp.value.toTimeZone(timeZone);
    // ... but that might turn a valid datetime into an invalid one:
    if (!tmp.value.isValid() && tmp.state == Acceptable)
        tmp.state = Intermediate;

    position += tmp.padded;
    state = QValidator::State(int(tmp.state));
    if (state == QValidator::Acceptable) {
        if (tmp.conflicts && conflictGuard != tmp.value) {
            conflictGuard = tmp.value;
            clearCache();
            input = textFromValue(tmp.value);
            updateCache(tmp.value, input);
            conflictGuard.clear();
        } else {
            cachedText = input;
            cachedState = state;
            cachedValue = tmp.value;
        }
    } else {
        clearCache();
    }
    return (tmp.value.isNull() ? getZeroVariant().toDateTime() : tmp.value);
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

//  from src/widgets/widgets/qabstractspinbox.cpp, line 1456, as _ZNK23QAbstractSpinBoxPrivate12specialValueEv
inline bool QAbstractSpinBoxPrivate::specialValue() const
{
    return (value == minimum && !specialValueText.isEmpty());
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2586, as _ZN14QCalendarPopup22verifyCalendarInstanceEv
inline QCalendarWidget *QCalendarPopup::verifyCalendarInstance()
{
    if (calendar.isNull()) {
        QCalendarWidget *cw = new QCalendarWidget(this);
        cw->setCalendar(calendarSystem);
        cw->setVerticalHeaderFormat(QCalendarWidget::NoVerticalHeader);
        setCalendarWidget(cw);
        return cw;
    } else {
        return calendar.data();
    }
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

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2599, as _ZN14QCalendarPopup17setCalendarWidgetEP15QCalendarWidget
inline void QCalendarPopup::setCalendarWidget(QCalendarWidget *cw)
{
    Q_ASSERT(cw);
    QVBoxLayout *widgetLayout = qobject_cast<QVBoxLayout*>(layout());
    if (!widgetLayout) {
        widgetLayout = new QVBoxLayout(this);
        widgetLayout->setContentsMargins(QMargins());
        widgetLayout->setSpacing(0);
    }
    delete calendar.data();
    calendar = QPointer<QCalendarWidget>(cw);
    widgetLayout->addWidget(cw);

    connect(cw, SIGNAL(activated(QDate)), this, SLOT(dateSelected(QDate)));
    connect(cw, SIGNAL(clicked(QDate)), this, SLOT(dateSelected(QDate)));
    connect(cw, SIGNAL(selectionChanged()), this, SLOT(dateSelectionChanged()));

    cw->setFocus();
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2239, as _ZN20QDateTimeEditPrivate18readLocaleSettingsEv
inline void QDateTimeEditPrivate::readLocaleSettings()
{
    const QLocale loc;
    defaultTimeFormat = loc.timeFormat(QLocale::ShortFormat);
    defaultDateFormat = loc.dateFormat(QLocale::ShortFormat);
    defaultDateTimeFormat = loc.dateTimeFormat(QLocale::ShortFormat);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2139, as _ZN20QDateTimeEditPrivate11emitSignalsE10EmitPolicyRK8QVariant
inline void QDateTimeEditPrivate::emitSignals(EmitPolicy ep, const QVariant &old)
{
    Q_Q(QDateTimeEdit);
    if (ep == NeverEmit) {
        return;
    }
    pendingEmit = false;

    const bool dodate = value.toDate().isValid() && (sections & DateSectionMask);
    const bool datechanged = (ep == AlwaysEmit || old.toDate() != value.toDate());
    const bool dotime = value.toTime().isValid() && (sections & TimeSectionMask);
    const bool timechanged = (ep == AlwaysEmit || old.toTime() != value.toTime());

    updateCache(value, displayText());

    syncCalendarWidget();
    if (datechanged || timechanged)
        emit q->dateTimeChanged(value.toDateTime());
    if (dodate && datechanged)
        emit q->dateChanged(value.toDate());
    if (dotime && timechanged)
        emit q->timeChanged(value.toTime());

}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1941, as _ZNK20QDateTimeEditPrivate13textFromValueERK8QVariant
inline QString QDateTimeEditPrivate::textFromValue(const QVariant &f) const
{
    Q_Q(const QDateTimeEdit);
    return q->textFromDateTime(f.toDateTime());
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1954, as _ZNK20QDateTimeEditPrivate13valueFromTextERK7QString
inline QVariant QDateTimeEditPrivate::valueFromText(const QString &f) const
{
    Q_Q(const QDateTimeEdit);
    return q->dateTimeFromText(f).toTimeZone(timeZone);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2338, as _ZN20QDateTimeEditPrivate9interpretE10EmitPolicy
inline void QDateTimeEditPrivate::interpret(EmitPolicy ep)
{
    Q_Q(QDateTimeEdit);
    QString tmp = displayText();
    int pos = edit->cursorPosition();
    const QValidator::State state = q->validate(tmp, pos);
    if (state != QValidator::Acceptable
        && correctionMode == QAbstractSpinBox::CorrectToPreviousValue
        && (state == QValidator::Invalid
            || currentSectionIndex < 0
            || !(fieldInfo(currentSectionIndex) & AllowPartial))) {
        setValue(value, ep);
        updateTimeZone();
    } else {
        QAbstractSpinBoxPrivate::interpret(ep);
    }
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2356, as _ZNK20QDateTimeEditPrivate10clearCacheEv
inline void QDateTimeEditPrivate::clearCache() const
{
    QAbstractSpinBoxPrivate::clearCache();
    cachedDay = -1;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2446, as _ZN20QDateTimeEditPrivate15newHoverControlERK6QPoint
inline QStyle::SubControl QDateTimeEditPrivate::newHoverControl(const QPoint &pos)
{
    if (!calendarPopupEnabled())
        return QAbstractSpinBoxPrivate::newHoverControl(pos);

    Q_Q(QDateTimeEdit);

    QStyleOptionComboBox optCombo;
    optCombo.initFrom(q);
    optCombo.editable = true;
    optCombo.subControls = QStyle::SC_All;
    hoverControl = q->style()->hitTestComplexControl(QStyle::CC_ComboBox, &optCombo, pos, q);
    return hoverControl;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2461, as _ZN20QDateTimeEditPrivate23updateEditFieldGeometryEv
inline void QDateTimeEditPrivate::updateEditFieldGeometry()
{
    if (!calendarPopupEnabled()) {
        QAbstractSpinBoxPrivate::updateEditFieldGeometry();
        return;
    }

    Q_Q(QDateTimeEdit);

    QStyleOptionComboBox optCombo;
    optCombo.initFrom(q);
    optCombo.editable = true;
    optCombo.subControls = QStyle::SC_ComboBoxEditField;
    edit->setGeometry(q->style()->subControlRect(QStyle::CC_ComboBox, &optCombo,
                                                 QStyle::SC_ComboBoxEditField, q));
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2478, as _ZNK20QDateTimeEditPrivate14getZeroVariantEv
inline QVariant QDateTimeEditPrivate::getZeroVariant() const
{
    Q_ASSERT(type == QMetaType::QDateTime);
    return QDATETIMEEDIT_DATE_INITIAL.startOfDay(timeZone);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2484, as _ZN20QDateTimeEditPrivate8setRangeERK8QVariantS2_
inline void QDateTimeEditPrivate::setRange(const QVariant &min, const QVariant &max)
{
    QAbstractSpinBoxPrivate::setRange(min, max);
    syncCalendarWidget();
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1675, as _ZNK20QDateTimeEditPrivate10getMinimumERK9QTimeZone
inline QDateTime QDateTimeEditPrivate::getMinimum(const QTimeZone &zone) const
{
    if (keyboardTracking)
        return minimum.toDateTime().toTimeZone(zone);

    // QDTP's min is the local-time start of QDATETIMEEDIT_DATE_MIN, cached
    // (along with its conversion to UTC).
    if (timeZone.timeSpec() == Qt::LocalTime)
        return QDateTimeParser::getMinimum(zone);

    return QDATETIMEEDIT_DATE_MIN.startOfDay(timeZone).toTimeZone(zone);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1688, as _ZNK20QDateTimeEditPrivate10getMaximumERK9QTimeZone
inline QDateTime QDateTimeEditPrivate::getMaximum(const QTimeZone &zone) const
{
    if (keyboardTracking)
        return maximum.toDateTime().toTimeZone(zone);

    // QDTP's max is the local-time end of QDATETIMEEDIT_DATE_MAX, cached
    // (along with its conversion to UTC).
    if (timeZone.timeSpec() == Qt::LocalTime)
        return QDateTimeParser::getMaximum(zone);

    return QDATETIMEEDIT_DATE_MAX.endOfDay(timeZone).toTimeZone(zone);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2323, as _ZNK20QDateTimeEditPrivate13absoluteIndexEN13QDateTimeEdit7SectionEi
inline int QDateTimeEditPrivate::absoluteIndex(QDateTimeEdit::Section s, int index) const
{
    for (int i=0; i<sectionNodes.size(); ++i) {
        if (convertToPublic(sectionNodes.at(i).type) == s && index-- == 0) {
            return i;
        }
    }
    return NoSectionIndex;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2333, as _ZNK20QDateTimeEditPrivate13absoluteIndexEN15QDateTimeParser11SectionNodeE
inline int QDateTimeEditPrivate::absoluteIndex(SectionNode s) const
{
    return sectionNodes.indexOf(s);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1971, as _ZNK20QDateTimeEditPrivate6stepByEiib
inline QDateTime QDateTimeEditPrivate::stepBy(int sectionIndex, int steps, bool test) const
{
    Q_Q(const QDateTimeEdit);
    QDateTime v = value.toDateTime();
    QString str = displayText();
    int pos = edit->cursorPosition();
    const SectionNode sn = sectionNode(sectionIndex);

    // to make sure it behaves reasonably when typing something and then stepping in non-tracking mode
    if (!test && pendingEmit && q->validate(str, pos) == QValidator::Acceptable)
        v = q->dateTimeFromText(str);
    int val = getDigit(v, sectionIndex);

    const int min = absoluteMin(sectionIndex);
    const int max = absoluteMax(sectionIndex, value.toDateTime());

    if (sn.type & DayOfWeekSectionMask) {
        // Must take locale's first day of week into account when *not*
        // wrapping; min and max don't help us.
#ifndef QT_ALWAYS_WRAP_WEEKDAY // (documentation, not an actual define)
        if (!wrapping) {
            /* It's not clear this is ever really a desirable behavior.

               It refuses to step backwards from the first day of the week or
               forwards from the day before, only allowing day-of-week stepping
               from start to end of one week. That's strictly what non-wrapping
               behavior must surely mean, when put in locale-neutral terms.

               It is, however, likely that users would prefer the "more natural"
               behavior of cycling through the week.
            */
            const int first = int(locale().firstDayOfWeek()); // Mon = 1 through 7 = Sun
            val = qBound(val < first ? first - 7 : first,
                         val + steps,
                         val < first ? first - 1 : first + 6);
        } else
#endif
        {
            val += steps;
        }

        // Restore to range from 1 through 7:
        val = val % 7;
        if (val <= 0)
            val += 7;
    } else {
        val += steps;
        const int span = max - min + 1;
        if (val < min)
            val = wrapping ? val + span : min;
        else if (val > max)
            val = wrapping ? val - span : max;
    }

    const int oldDay = v.date().day(calendar);

    /*
        Stepping into a daylight saving time that doesn't exist (setDigit() is
        true when date and time are valid, even if the date-time returned
        isn't), so use the time that has the same distance from epoch.
    */
    if (setDigit(v, sectionIndex, val) && getDigit(v, sectionIndex) != val
        && sn.type & HourSectionMask && steps < 0) {
        // decreasing from e.g 3am to 2am would get us back to 3am, but we want 1am
        auto msecsSinceEpoch = v.toMSecsSinceEpoch() - 3600 * 1000;
        v = QDateTime::fromMSecsSinceEpoch(msecsSinceEpoch, v.timeRepresentation());
    }
    // if this sets year or month it will make
    // sure that days are lowered if needed.

    const QDateTime minimumDateTime = minimum.toDateTime();
    const QDateTime maximumDateTime = maximum.toDateTime();
    // changing one section should only modify that section, if possible
    if (sn.type != AmPmSection && !(sn.type & DayOfWeekSectionMask)
        && (v < minimumDateTime || v > maximumDateTime)) {
        const int localmin = getDigit(minimumDateTime, sectionIndex);
        const int localmax = getDigit(maximumDateTime, sectionIndex);

        if (wrapping) {
            // just because we hit the roof in one direction, it
            // doesn't mean that we hit the floor in the other
            if (steps > 0) {
                setDigit(v, sectionIndex, min);
                if (!(sn.type & DaySectionMask) && sections & DateSectionMask) {
                    const int daysInMonth = v.date().daysInMonth(calendar);
                    if (v.date().day(calendar) < oldDay && v.date().day(calendar) < daysInMonth) {
                        const int adds = qMin(oldDay, daysInMonth);
                        v = v.addDays(adds - v.date().day(calendar));
                    }
                }

                if (v < minimumDateTime) {
                    setDigit(v, sectionIndex, localmin);
                    if (v < minimumDateTime)
                        setDigit(v, sectionIndex, localmin + 1);
                }
            } else {
                setDigit(v, sectionIndex, max);
                if (!(sn.type & DaySectionMask) && sections & DateSectionMask) {
                    const int daysInMonth = v.date().daysInMonth(calendar);
                    if (v.date().day(calendar) < oldDay && v.date().day(calendar) < daysInMonth) {
                        const int adds = qMin(oldDay, daysInMonth);
                        v = v.addDays(adds - v.date().day(calendar));
                    }
                }

                if (v > maximumDateTime) {
                    setDigit(v, sectionIndex, localmax);
                    if (v > maximumDateTime)
                        setDigit(v, sectionIndex, localmax - 1);
                }
            }
        } else {
            setDigit(v, sectionIndex, (steps > 0 ? localmax : localmin));
        }
    }
    if (!test && oldDay != v.date().day(calendar) && !(sn.type & DaySectionMask)) {
        // this should not happen when called from stepEnabled
        cachedDay = qMax<int>(oldDay, cachedDay);
    }

    if (v < minimumDateTime) {
        if (wrapping) {
            QDateTime t = v;
            setDigit(t, sectionIndex, steps < 0 ? max : min);
            bool mincmp = (t >= minimumDateTime);
            bool maxcmp = (t <= maximumDateTime);
            if (!mincmp || !maxcmp) {
                setDigit(t, sectionIndex, getDigit(steps < 0
                                                   ? maximumDateTime
                                                   : minimumDateTime, sectionIndex));
                mincmp = (t >= minimumDateTime);
                maxcmp = (t <= maximumDateTime);
            }
            if (mincmp && maxcmp) {
                v = t;
            }
        } else {
            v = value.toDateTime();
        }
    } else if (v > maximumDateTime) {
        if (wrapping) {
            QDateTime t = v;
            setDigit(t, sectionIndex, steps > 0 ? min : max);
            bool mincmp = (t >= minimumDateTime);
            bool maxcmp = (t <= maximumDateTime);
            if (!mincmp || !maxcmp) {
                setDigit(t, sectionIndex, getDigit(steps > 0 ?
                                                   minimumDateTime :
                                                   maximumDateTime, sectionIndex));
                mincmp = (t >= minimumDateTime);
                maxcmp = (t <= maximumDateTime);
            }
            if (mincmp && maxcmp) {
                v = t;
            }
        } else {
            v = value.toDateTime();
        }
    }

    return bound(std::move(v), value, steps).toDateTime().toTimeZone(timeZone);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1732, as _ZNK20QDateTimeEditPrivate9sectionAtEi
inline int QDateTimeEditPrivate::sectionAt(int pos) const
{
    if (pos < separators.first().size())
        return (pos == 0 ? FirstSectionIndex : NoSectionIndex);

    const QString text = displayText();
    const int textSize = text.size();
    if (textSize - pos < separators.last().size() + 1) {
        if (separators.last().size() == 0) {
            return sectionNodes.size() - 1;
        }
        return (pos == textSize ? LastSectionIndex : NoSectionIndex);
    }
    updateCache(value, text);

    for (int i=0; i<sectionNodes.size(); ++i) {
        const int tmp = sectionPos(i);
        if (pos < tmp + sectionSize(i)) {
            return (pos < tmp ? -1 : i);
        }
    }
    return -1;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1763, as _ZNK20QDateTimeEditPrivate14closestSectionEib
inline int QDateTimeEditPrivate::closestSection(int pos, bool forward) const
{
    Q_ASSERT(pos >= 0);
    if (pos < separators.first().size())
        return forward ? 0 : FirstSectionIndex;

    const QString text = displayText();
    if (text.size() - pos < separators.last().size() + 1)
        return forward ? LastSectionIndex : int(sectionNodes.size() - 1);

    updateCache(value, text);
    for (int i=0; i<sectionNodes.size(); ++i) {
        const int tmp = sectionPos(sectionNodes.at(i));
        if (pos < tmp + sectionSize(i)) {
            if (pos < tmp && !forward) {
                return i-1;
            }
            return i;
        } else if (i == sectionNodes.size() - 1 && pos > tmp) {
            return i;
        }
    }
    qWarning("QDateTimeEdit: Internal Error: closestSection returned NoSection");
    return NoSectionIndex;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1795, as _ZNK20QDateTimeEditPrivate15nextPrevSectionEib
inline int QDateTimeEditPrivate::nextPrevSection(int current, bool forward) const
{
    Q_Q(const QDateTimeEdit);
    if (q->isRightToLeft())
        forward = !forward;

    switch (current) {
    case FirstSectionIndex: return forward ? 0 : FirstSectionIndex;
    case LastSectionIndex: return (forward ? LastSectionIndex : int(sectionNodes.size() - 1));
    case NoSectionIndex: return FirstSectionIndex;
    default: break;
    }
    Q_ASSERT(current >= 0 && current < sectionNodes.size());

    current += (forward ? 1 : -1);
    if (current >= sectionNodes.size()) {
        return LastSectionIndex;
    } else if (current < 0) {
        return FirstSectionIndex;
    }

    return current;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1707, as _ZN20QDateTimeEditPrivate11setSelectedEib
inline void QDateTimeEditPrivate::setSelected(int sectionIndex, bool forward)
{
    if (specialValue()) {
        edit->selectAll();
    } else {
        const SectionNode &node = sectionNode(sectionIndex);
        if (node.type == NoSection || node.type == LastSection || node.type == FirstSection)
            return;

        updateCache(value, displayText());
        const int size = sectionSize(sectionIndex);
        if (forward) {
            edit->setSelection(sectionPos(node), size);
        } else {
            edit->setSelection(sectionPos(node) + size, -size);
        }
    }
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1850, as _ZNK20QDateTimeEditPrivate11updateCacheERK8QVariantRK7QString
inline void QDateTimeEditPrivate::updateCache(const QVariant &val, const QString &str) const
{
    if (val != cachedValue || str != cachedText || cacheGuard) {
        cacheGuard = true;
        QString copy = str;
        int unused = edit->cursorPosition();
        QValidator::State unusedState;
        validateAndInterpret(copy, unused, unusedState);
        cacheGuard = false;
    }
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1623, as _ZN20QDateTimeEditPrivate15convertTimeZoneERK9QDateTime
inline QDateTime QDateTimeEditPrivate::convertTimeZone(const QDateTime &datetime)
{
    return datetime.toTimeZone(timeZone);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1633, as _ZN20QDateTimeEditPrivate14updateTimeZoneEv
inline void QDateTimeEditPrivate::updateTimeZone()
{
    minimum = minimum.toDateTime().toTimeZone(timeZone);
    maximum = maximum.toDateTime().toTimeZone(timeZone);
    value = value.toDateTime().toTimeZone(timeZone);

    // time zone changes can lead to 00:00:00 becomes 01:00:00 and 23:59:59 becomes 00:59:59 (invalid range)
    const bool dateShown = (sections & QDateTimeEdit::DateSections_Mask);
    if (!dateShown) {
        if (minimum.toTime() >= maximum.toTime()){
            minimum = value.toDate().startOfDay(timeZone);
            maximum = value.toDate().endOfDay(timeZone);
        }
    }
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 1628, as _ZNK20QDateTimeEditPrivate13dateTimeValueE5QDate5QTime
inline QDateTime QDateTimeEditPrivate::dateTimeValue(QDate date, QTime time) const
{
    return QDateTime(date, time, timeZone);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2420, as _ZN20QDateTimeEditPrivate14_q_resetButtonEv
inline void QDateTimeEditPrivate::_q_resetButton()
{
    updateArrow(QStyle::State_None);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2425, as _ZN20QDateTimeEditPrivate11updateArrowEN6QStyle9StateFlagE
inline void QDateTimeEditPrivate::updateArrow(QStyle::StateFlag state)
{
    Q_Q(QDateTimeEdit);

    if (arrowState == state)
        return;
    arrowState = state;
    if (arrowState != QStyle::State_None)
        buttonState |= Mouse;
    else {
        buttonState = 0;
        hoverControl = QStyle::SC_ComboBoxFrame;
    }
    q->update();
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2558, as _ZNK20QDateTimeEditPrivate20calendarPopupEnabledEv
inline bool QDateTimeEditPrivate::calendarPopupEnabled() const
{
    return (calendarPopup && (sections & (DateSectionMask)));
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2563, as _ZN20QDateTimeEditPrivate18syncCalendarWidgetEv
inline void QDateTimeEditPrivate::syncCalendarWidget()
{
    Q_Q(QDateTimeEdit);
    if (monthCalendar) {
        const QSignalBlocker blocker(monthCalendar);
        monthCalendar->setDateRange(q->minimumDate(), q->maximumDate());
        monthCalendar->setDate(q->date());
    }
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2491, as _ZNK20QDateTimeEditPrivate14isSeparatorKeyEPK9QKeyEvent
inline bool QDateTimeEditPrivate::isSeparatorKey(const QKeyEvent *ke) const
{
    if (!ke->text().isEmpty() && currentSectionIndex + 1 < sectionNodes.size() && currentSectionIndex >= 0) {
        if (fieldInfo(currentSectionIndex) & Numeric) {
            if (ke->text().at(0).isNumber())
                return false;
        } else if (ke->text().at(0).isLetterOrNumber()) {
            return false;
        }
        return separators.at(currentSectionIndex + 1).contains(ke->text());
    }
    return false;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2269, as _ZN20QDateTimeEditPrivate15convertSectionsE6QFlagsIN15QDateTimeParser7SectionEE
inline QDateTimeEdit::Sections QDateTimeEditPrivate::convertSections(QDateTimeParser::Sections s)
{
    QDateTimeEdit::Sections ret;
    if (s & QDateTimeParser::MSecSection)
        ret |= QDateTimeEdit::MSecSection;
    if (s & QDateTimeParser::SecondSection)
        ret |= QDateTimeEdit::SecondSection;
    if (s & QDateTimeParser::MinuteSection)
        ret |= QDateTimeEdit::MinuteSection;
    if (s & (QDateTimeParser::HourSectionMask))
        ret |= QDateTimeEdit::HourSection;
    if (s & QDateTimeParser::AmPmSection)
        ret |= QDateTimeEdit::AmPmSection;
    if (s & (QDateTimeParser::DaySectionMask))
        ret |= QDateTimeEdit::DaySection;
    if (s & QDateTimeParser::MonthSection)
        ret |= QDateTimeEdit::MonthSection;
    if (s & (QDateTimeParser::YearSectionMask))
        ret |= QDateTimeEdit::YearSection;

    return ret;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2247, as _ZN20QDateTimeEditPrivate15convertToPublicEN15QDateTimeParser7SectionE
inline QDateTimeEdit::Section QDateTimeEditPrivate::convertToPublic(QDateTimeParser::Section s)
{
    switch (s & ~Internal) {
    case AmPmSection: return QDateTimeEdit::AmPmSection;
    case MSecSection: return QDateTimeEdit::MSecSection;
    case SecondSection: return QDateTimeEdit::SecondSection;
    case MinuteSection: return QDateTimeEdit::MinuteSection;
    case DayOfWeekSectionShort:
    case DayOfWeekSectionLong:
    case DaySection: return QDateTimeEdit::DaySection;
    case MonthSection: return QDateTimeEdit::MonthSection;
    case YearSection2Digits:
    case YearSection: return QDateTimeEdit::YearSection;
    case Hour12Section:
    case Hour24Section: return QDateTimeEdit::HourSection;
    case FirstSection:
    case NoSection:
    case LastSection: break;
    }
    return QDateTimeEdit::NoSection;
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2522, as _ZN20QDateTimeEditPrivate21positionCalendarPopupEv
inline void QDateTimeEditPrivate::positionCalendarPopup()
{
    Q_Q(QDateTimeEdit);
    QPoint pos = (q->layoutDirection() == Qt::RightToLeft) ? q->rect().bottomRight() : q->rect().bottomLeft();
    QPoint pos2 = (q->layoutDirection() == Qt::RightToLeft) ? q->rect().topRight() : q->rect().topLeft();
    pos = q->mapToGlobal(pos);
    pos2 = q->mapToGlobal(pos2);
    QSize size = monthCalendar->sizeHint();
    QScreen *screen = QGuiApplication::screenAt(pos);
    if (!screen)
        screen = QGuiApplication::primaryScreen();
    const QRect screenRect = screen->availableGeometry();
    //handle popup falling "off screen"
    if (q->layoutDirection() == Qt::RightToLeft) {
        pos.setX(pos.x()-size.width());
        pos2.setX(pos2.x()-size.width());
        if (pos.x() < screenRect.left())
            pos.setX(qMax(pos.x(), screenRect.left()));
        else if (pos.x()+size.width() > screenRect.right())
            pos.setX(qMax(pos.x()-size.width(), screenRect.right()-size.width()));
    } else {
        if (pos.x()+size.width() > screenRect.right())
            pos.setX(screenRect.right()-size.width());
        pos.setX(qMax(pos.x(), screenRect.left()));
    }
    if (pos.y() + size.height() > screenRect.bottom())
        pos.setY(pos2.y() - size.height());
    else if (pos.y() < screenRect.top())
        pos.setY(screenRect.top());
    if (pos.y() < screenRect.top())
        pos.setY(screenRect.top());
    if (pos.y()+size.height() > screenRect.bottom())
        pos.setY(screenRect.bottom()-size.height());
    monthCalendar->move(pos);
}
//  -----------------------------------------------------------------------

//  A QDateTimeEditPrivate that Python can take functions over in. Every QDateTimeEditPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(spinbox)
typedef void (*CuteQDateTimeEditPrivateCall0)(const void *, int, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQDateTimeEditPrivateCall1)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQDateTimeEditPrivateCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDateTimeEditPrivateCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDateTimeEditPrivateCall4)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDateTimeEditPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef int (*CuteQDateTimeEditPrivateCall6)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDateTimeEditPrivateCall7)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQDateTimeEditPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDateTimeEditPrivateCall9)(const void *, const QVariant *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef void (*CuteQDateTimeEditPrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(datetimeparser)
typedef QString * (*CuteQDateTimeEditPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
typedef const QDateTime * (*CuteQDateTimeEditPrivateCall12)(const void *, const QTimeZone *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
typedef const QDateTime * (*CuteQDateTimeEditPrivateCall13)(const void *, const QTimeZone *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
typedef const QLocale * (*CuteQDateTimeEditPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
typedef int (*CuteQDateTimeEditPrivateCall15)(const void *, int *);
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQDateTimeEditPrivateCall16)(const void *, const QVariant *, const QVariant *, int, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQDateTimeEditPrivateCall17)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQDateTimeEditPrivateCall18)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
typedef void (*CuteQDateTimeEditPrivateCall19)(const void *, bool, int *);
typedef void (*CuteQDateTimeEditPrivateCall20)(const void *, int, int *);
typedef void (*CuteQDateTimeEditPrivateCall21)(const void *, int *);
typedef void (*CuteQDateTimeEditPrivateCall22)(const void *, int *);
typedef void * (*CuteQDateTimeEditPrivateCall23)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQDateTimeEditPrivateCall24)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQDateTimeEditPrivateCall25)(const void *, int *);
typedef int (*CuteQDateTimeEditPrivateCall26)(const void *, int *);
typedef const QImage * (*CuteQDateTimeEditPrivateCall27)(const void *, int *);
typedef void (*CuteQDateTimeEditPrivateCall28)(const void *, int *);
typedef void (*CuteQDateTimeEditPrivateCall29)(const void *, int *);
typedef void (*CuteQDateTimeEditPrivateCall30)(const void *, int *);
typedef void (*CuteQDateTimeEditPrivateCall31)(const void *, int *);
typedef void (*CuteQDateTimeEditPrivateCall32)(const void *, int *);
typedef void (*CuteQDateTimeEditPrivateCall33)(const void *, int *);
typedef void (*CuteQDateTimeEditPrivateCall34)(const void *, int *);
typedef bool (*CuteQDateTimeEditPrivateCall35)(const void *, int *);
typedef bool (*CuteQDateTimeEditPrivateCall36)(const void *, int *);
class CuteQDateTimeEditPrivate : public QDateTimeEditPrivate {
public:
  using QDateTimeEditPrivate::QDateTimeEditPrivate;
  void *taken[37] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate11emitSignalsE10EmitPolicyRK8QVariant")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate13textFromValueERK8QVariant")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate13valueFromTextERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate27editorCursorPositionChangedEii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate9interpretE10EmitPolicy")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate10clearCacheEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate15newHoverControlERK6QPoint")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate23updateEditFieldGeometryEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate14getZeroVariantEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate8setRangeERK8QVariantS2_")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN23QAbstractSpinBoxPrivate10updateEditEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser11displayTextEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser10getMinimumERK9QTimeZone")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser10getMaximumERK9QTimeZone")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser6localeEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
    if (!std::strcmp(key, "_ZNK15QDateTimeParser14cursorPositionEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(datetimeparser)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate5boundERK8QVariantS2_i")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate10roundValueERK8QVariant")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK23QAbstractSpinBoxPrivate28calculateAdaptiveDecimalStepEi")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[36] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(spinbox)
  //  void QDateTimeEditPrivate::emitSignals(EmitPolicy ep, const QVariant
  //      &old)
  void emitSignals(EmitPolicy ep, const QVariant &old) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall0 call = reinterpret_cast<CuteQDateTimeEditPrivateCall0>(taken[0]);
      call(this, static_cast<int>(ep), &old, &handled);
      if (handled) return;
    }
    QDateTimeEditPrivate::emitSignals(ep, old);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QString QDateTimeEditPrivate::textFromValue(const QVariant &f) const
  QString textFromValue(const QVariant &f) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall1 call = reinterpret_cast<CuteQDateTimeEditPrivateCall1>(taken[1]);
      QString * given = call(this, &f, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDateTimeEditPrivate::textFromValue(f);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QVariant QDateTimeEditPrivate::valueFromText(const QString &f) const
  QVariant valueFromText(const QString &f) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall2 call = reinterpret_cast<CuteQDateTimeEditPrivateCall2>(taken[2]);
      const QVariant * given = call(this, &f, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeEditPrivate::valueFromText(f);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QDateTimeEditPrivate::editorCursorPositionChanged(int oldpos,
  //      int newpos)
  void editorCursorPositionChanged(int oldpos, int newpos) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall3 call = reinterpret_cast<CuteQDateTimeEditPrivateCall3>(taken[3]);
      call(this, oldpos, newpos, &handled);
      if (handled) return;
    }
    QDateTimeEditPrivate::editorCursorPositionChanged(oldpos, newpos);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QDateTimeEditPrivate::interpret(EmitPolicy ep)
  void interpret(EmitPolicy ep) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall4 call = reinterpret_cast<CuteQDateTimeEditPrivateCall4>(taken[4]);
      call(this, static_cast<int>(ep), &handled);
      if (handled) return;
    }
    QDateTimeEditPrivate::interpret(ep);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QDateTimeEditPrivate::clearCache() const
  void clearCache() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall5 call = reinterpret_cast<CuteQDateTimeEditPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDateTimeEditPrivate::clearCache();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QStyle::SubControl QDateTimeEditPrivate::newHoverControl(const QPoint
  //      &pos)
  QStyle::SubControl newHoverControl(const QPoint &pos) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall6 call = reinterpret_cast<CuteQDateTimeEditPrivateCall6>(taken[6]);
      int given = call(this, &pos, &handled);
      if (handled) return static_cast<QStyle::SubControl>(given);
    }
    return QDateTimeEditPrivate::newHoverControl(pos);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QDateTimeEditPrivate::updateEditFieldGeometry()
  void updateEditFieldGeometry() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall7 call = reinterpret_cast<CuteQDateTimeEditPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDateTimeEditPrivate::updateEditFieldGeometry();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QVariant QDateTimeEditPrivate::getZeroVariant() const
  QVariant getZeroVariant() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall8 call = reinterpret_cast<CuteQDateTimeEditPrivateCall8>(taken[8]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeEditPrivate::getZeroVariant();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QDateTimeEditPrivate::setRange(const QVariant &min, const
  //      QVariant &max)
  void setRange(const QVariant &min, const QVariant &max) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall9 call = reinterpret_cast<CuteQDateTimeEditPrivateCall9>(taken[9]);
      call(this, &min, &max, &handled);
      if (handled) return;
    }
    QDateTimeEditPrivate::setRange(min, max);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  void QDateTimeEditPrivate::updateEdit()
  void updateEdit() override {
    if (taken[10]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall10 call = reinterpret_cast<CuteQDateTimeEditPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QDateTimeEditPrivate::updateEdit();
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(datetimeparser)
  //  QString QDateTimeEditPrivate::displayText() const
  QString displayText() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall11 call = reinterpret_cast<CuteQDateTimeEditPrivateCall11>(taken[11]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDateTimeEditPrivate::displayText();
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(datetimeparser)
  //  QDateTime QDateTimeEditPrivate::getMinimum(const QTimeZone &zone)
  //      const
  QDateTime getMinimum(const QTimeZone &zone) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall12 call = reinterpret_cast<CuteQDateTimeEditPrivateCall12>(taken[12]);
      const QDateTime * given = call(this, &zone, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeEditPrivate::getMinimum(zone);
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(datetimeparser)
  //  QDateTime QDateTimeEditPrivate::getMaximum(const QTimeZone &zone)
  //      const
  QDateTime getMaximum(const QTimeZone &zone) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall13 call = reinterpret_cast<CuteQDateTimeEditPrivateCall13>(taken[13]);
      const QDateTime * given = call(this, &zone, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeEditPrivate::getMaximum(zone);
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(datetimeparser)
  //  QLocale QDateTimeEditPrivate::locale() const
  QLocale locale() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall14 call = reinterpret_cast<CuteQDateTimeEditPrivateCall14>(taken[14]);
      const QLocale * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDateTimeEditPrivate::locale();
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(datetimeparser)
  //  int QDateTimeEditPrivate::cursorPosition() const
  int cursorPosition() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall15 call = reinterpret_cast<CuteQDateTimeEditPrivateCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDateTimeEditPrivate::cursorPosition();
  }
#endif  // QT_CONFIG(datetimeparser)

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBoxPrivate::bound(const QVariant &val, const
  //      QVariant &old, int steps) const
  QVariant bound(
      const QVariant &val,
      const QVariant &old,
      int steps) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall16 call = reinterpret_cast<CuteQDateTimeEditPrivateCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall17 call = reinterpret_cast<CuteQDateTimeEditPrivateCall17>(taken[17]);
      const QVariant * given = call(this, &val, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBoxPrivate::roundValue(val);
  }
#endif  // QT_CONFIG(spinbox)

#if QT_CONFIG(spinbox)
  //  QVariant QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(int
  //      steps) const
  QVariant calculateAdaptiveDecimalStep(int steps) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall18 call = reinterpret_cast<CuteQDateTimeEditPrivateCall18>(taken[18]);
      const QVariant * given = call(this, steps, &handled);
      if (handled && given) return *given;
    }
    return QAbstractSpinBoxPrivate::calculateAdaptiveDecimalStep(steps);
  }
#endif  // QT_CONFIG(spinbox)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall19 call = reinterpret_cast<CuteQDateTimeEditPrivateCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall20 call = reinterpret_cast<CuteQDateTimeEditPrivateCall20>(taken[20]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[21]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall21 call = reinterpret_cast<CuteQDateTimeEditPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[22]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall22 call = reinterpret_cast<CuteQDateTimeEditPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[23]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall23 call = reinterpret_cast<CuteQDateTimeEditPrivateCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall24 call = reinterpret_cast<CuteQDateTimeEditPrivateCall24>(taken[24]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall25 call = reinterpret_cast<CuteQDateTimeEditPrivateCall25>(taken[25]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[26]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall26 call = reinterpret_cast<CuteQDateTimeEditPrivateCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[27]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall27 call = reinterpret_cast<CuteQDateTimeEditPrivateCall27>(taken[27]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall28 call = reinterpret_cast<CuteQDateTimeEditPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[29]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall29 call = reinterpret_cast<CuteQDateTimeEditPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall30 call = reinterpret_cast<CuteQDateTimeEditPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[31]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall31 call = reinterpret_cast<CuteQDateTimeEditPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall32 call = reinterpret_cast<CuteQDateTimeEditPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[33]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall33 call = reinterpret_cast<CuteQDateTimeEditPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[34]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall34 call = reinterpret_cast<CuteQDateTimeEditPrivateCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[35]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall35 call = reinterpret_cast<CuteQDateTimeEditPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[36]) {
      int handled = 0;
      CuteQDateTimeEditPrivateCall36 call = reinterpret_cast<CuteQDateTimeEditPrivateCall36>(taken[36]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QDateTimeEdit *QDateTimeEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDateTimeEdit *ritual_ZN20QDateTimeEditPrivate6q_funcEv(
    QDateTimeEditPrivate *self) {
  return self->q_func();
}

//  const QDateTimeEdit *QDateTimeEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDateTimeEdit *ritual_ZNK20QDateTimeEditPrivate6q_funcEv(
    const QDateTimeEditPrivate *self) {
  return self->q_func();
}

//  void QDateTimeEditPrivate::readLocaleSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate18readLocaleSettingsEv(
    QDateTimeEditPrivate *self) {
  self->readLocaleSettings();
}

//  void QDateTimeEditPrivate::emitSignals(EmitPolicy ep, const QVariant
//      &old)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate11emitSignalsE10EmitPolicyRK8QVariant(
    QDateTimeEditPrivate *self,
    EmitPolicy ep,
    const QVariant *old) {
  self->emitSignals(ep, *old);
}

//  QString QDateTimeEditPrivate::textFromValue(const QVariant &f) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDateTimeEditPrivate13textFromValueERK8QVariant(
    const QDateTimeEditPrivate *self,
    const QVariant *f) {
  return new QString(self->textFromValue(*f));
}

//  QVariant QDateTimeEditPrivate::valueFromText(const QString &f) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QDateTimeEditPrivate13valueFromTextERK7QString(
    const QDateTimeEditPrivate *self,
    const QString *f) {
  return new QVariant(self->valueFromText(*f));
}

//  void QDateTimeEditPrivate::interpret(EmitPolicy ep)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate9interpretE10EmitPolicy(
    QDateTimeEditPrivate *self,
    EmitPolicy ep) {
  self->interpret(ep);
}

//  void QDateTimeEditPrivate::clearCache() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QDateTimeEditPrivate10clearCacheEv(
    const QDateTimeEditPrivate *self) {
  self->clearCache();
}

//  QStyle::SubControl QDateTimeEditPrivate::newHoverControl(const QPoint
//      &pos)
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_ZN20QDateTimeEditPrivate15newHoverControlERK6QPoint(
    QDateTimeEditPrivate *self,
    const QPoint *pos) {
  return self->newHoverControl(*pos);
}

//  void QDateTimeEditPrivate::updateEditFieldGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate23updateEditFieldGeometryEv(
    QDateTimeEditPrivate *self) {
  self->updateEditFieldGeometry();
}

//  QVariant QDateTimeEditPrivate::getZeroVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QDateTimeEditPrivate14getZeroVariantEv(
    const QDateTimeEditPrivate *self) {
  return new QVariant(self->getZeroVariant());
}

//  void QDateTimeEditPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate8setRangeERK8QVariantS2_(
    QDateTimeEditPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->setRange(*min, *max);
}

//  QString QDateTimeEditPrivate::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDateTimeEditPrivate11displayTextEv(
    const QDateTimeEditPrivate *self) {
  return new QString(self->displayText());
}

//  QDateTime QDateTimeEditPrivate::getMinimum(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK20QDateTimeEditPrivate10getMinimumERK9QTimeZone(
    const QDateTimeEditPrivate *self,
    const QTimeZone *zone) {
  return new QDateTime(self->getMinimum(*zone));
}

//  QDateTime QDateTimeEditPrivate::getMaximum(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK20QDateTimeEditPrivate10getMaximumERK9QTimeZone(
    const QDateTimeEditPrivate *self,
    const QTimeZone *zone) {
  return new QDateTime(self->getMaximum(*zone));
}

//  QLocale QDateTimeEditPrivate::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK20QDateTimeEditPrivate6localeEv(
    const QDateTimeEditPrivate *self) {
  return new QLocale(self->locale());
}

//  int QDateTimeEditPrivate::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDateTimeEditPrivate14cursorPositionEv(
    const QDateTimeEditPrivate *self) {
  return self->cursorPosition();
}

//  int QDateTimeEditPrivate::absoluteIndex(QDateTimeEdit::Section s, int
//      index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDateTimeEditPrivate13absoluteIndexEN13QDateTimeEdit7SectionEi(
    const QDateTimeEditPrivate *self,
    QDateTimeEdit::Section s,
    int index) {
  return self->absoluteIndex(s, index);
}

//  int QDateTimeEditPrivate::absoluteIndex(SectionNode s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDateTimeEditPrivate13absoluteIndexEN15QDateTimeParser11SectionNodeE(
    const QDateTimeEditPrivate *self,
    const QDateTimeParser::SectionNode *s) {
  return self->absoluteIndex(*s);
}

//  QDateTime QDateTimeEditPrivate::stepBy(int index, int steps, bool test)
//      const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK20QDateTimeEditPrivate6stepByEiib(
    const QDateTimeEditPrivate *self,
    int index,
    int steps,
    bool test) {
  return new QDateTime(self->stepBy(index, steps, test));
}

//  int QDateTimeEditPrivate::sectionAt(int pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDateTimeEditPrivate9sectionAtEi(
    const QDateTimeEditPrivate *self,
    int pos) {
  return self->sectionAt(pos);
}

//  int QDateTimeEditPrivate::closestSection(int index, bool forward) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDateTimeEditPrivate14closestSectionEib(
    const QDateTimeEditPrivate *self,
    int index,
    bool forward) {
  return self->closestSection(index, forward);
}

//  int QDateTimeEditPrivate::nextPrevSection(int index, bool forward) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDateTimeEditPrivate15nextPrevSectionEib(
    const QDateTimeEditPrivate *self,
    int index,
    bool forward) {
  return self->nextPrevSection(index, forward);
}

//  void QDateTimeEditPrivate::setSelected(int index, bool forward)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate11setSelectedEib(
    QDateTimeEditPrivate *self,
    int index,
    bool forward) {
  self->setSelected(index, forward);
}

//  void QDateTimeEditPrivate::updateCache(const QVariant &val, const QString
//      &str) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QDateTimeEditPrivate11updateCacheERK8QVariantRK7QString(
    const QDateTimeEditPrivate *self,
    const QVariant *val,
    const QString *str) {
  self->updateCache(*val, *str);
}

//  QDateTime QDateTimeEditPrivate::convertTimeZone(const QDateTime
//      &datetime)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN20QDateTimeEditPrivate15convertTimeZoneERK9QDateTime(
    QDateTimeEditPrivate *self,
    const QDateTime *datetime) {
  return new QDateTime(self->convertTimeZone(*datetime));
}

//  void QDateTimeEditPrivate::updateTimeZone()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate14updateTimeZoneEv(
    QDateTimeEditPrivate *self) {
  self->updateTimeZone();
}

//  QString QDateTimeEditPrivate::valueToText(const QVariant &var) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDateTimeEditPrivate11valueToTextERK8QVariant(
    const QDateTimeEditPrivate *self,
    const QVariant *var) {
  return new QString(self->valueToText(*var));
}

//  QDateTime QDateTimeEditPrivate::dateTimeValue(QDate date, QTime time)
//      const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK20QDateTimeEditPrivate13dateTimeValueE5QDate5QTime(
    const QDateTimeEditPrivate *self,
    const QDate *date,
    const QTime *time) {
  return new QDateTime(self->dateTimeValue(*date, *time));
}

//  void QDateTimeEditPrivate::_q_resetButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate14_q_resetButtonEv(
    QDateTimeEditPrivate *self) {
  self->_q_resetButton();
}

//  void QDateTimeEditPrivate::updateArrow(QStyle::StateFlag state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate11updateArrowEN6QStyle9StateFlagE(
    QDateTimeEditPrivate *self,
    QStyle::StateFlag state) {
  self->updateArrow(state);
}

//  bool QDateTimeEditPrivate::calendarPopupEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDateTimeEditPrivate20calendarPopupEnabledEv(
    const QDateTimeEditPrivate *self) {
  return self->calendarPopupEnabled();
}

//  void QDateTimeEditPrivate::syncCalendarWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate18syncCalendarWidgetEv(
    QDateTimeEditPrivate *self) {
  self->syncCalendarWidget();
}

//  bool QDateTimeEditPrivate::isSeparatorKey(const QKeyEvent *k) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDateTimeEditPrivate14isSeparatorKeyEPK9QKeyEvent(
    const QDateTimeEditPrivate *self,
    const QKeyEvent *k) {
  return self->isSeparatorKey(k);
}

//  QDateTimeEdit::Sections
//      QDateTimeEditPrivate::convertSections(QDateTimeParser::Sections s)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QDateTimeEditPrivate15convertSectionsE6QFlagsIN15QDateTimeParser7SectionEE(
    int s) {
  return static_cast<int>(
      QDateTimeEditPrivate::convertSections(
          QFlags<QDateTimeParser::Section>::fromInt(s)).toInt());
}

//  QDateTimeEdit::Section
//      QDateTimeEditPrivate::convertToPublic(QDateTimeParser::Section s)
extern "C" Q_DECL_EXPORT
QDateTimeEdit::Section ritual_ZN20QDateTimeEditPrivate15convertToPublicEN15QDateTimeParser7SectionE(
    QDateTimeParser::Section s) {
  return QDateTimeEditPrivate::convertToPublic(s);
}

//  void QDateTimeEditPrivate::positionCalendarPopup()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDateTimeEditPrivate21positionCalendarPopupEv(
    QDateTimeEditPrivate *self) {
  self->positionCalendarPopup();
}

//  QDateTimeEditPrivate as the QDateTimeParser it is built on
extern "C" Q_DECL_EXPORT
QDateTimeParser *ritual_cast_QDateTimeEditPrivate_QDateTimeParser(
    QDateTimeEditPrivate *self) {
  return static_cast<QDateTimeParser *>(self);
}

//  a Python function taken by a CuteQDateTimeEditPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDateTimeEditPrivate(
    QDateTimeEditPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDateTimeEditPrivate *>(self)->take(key, call);
}

//  void QDateTimeEditPrivate::emitSignals(EmitPolicy ep, const QVariant
//      &old)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeEditPrivate11emitSignalsE10EmitPolicyRK8QVariant(
    QDateTimeEditPrivate *self,
    EmitPolicy ep,
    const QVariant *old) {
  self->QDateTimeEditPrivate::emitSignals(ep, *old);
}

//  QString QDateTimeEditPrivate::textFromValue(const QVariant &f) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QDateTimeEditPrivate13textFromValueERK8QVariant(
    const QDateTimeEditPrivate *self,
    const QVariant *f) {
  return new QString(self->QDateTimeEditPrivate::textFromValue(*f));
}

//  QVariant QDateTimeEditPrivate::valueFromText(const QString &f) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QDateTimeEditPrivate13valueFromTextERK7QString(
    const QDateTimeEditPrivate *self,
    const QString *f) {
  return new QVariant(self->QDateTimeEditPrivate::valueFromText(*f));
}

//  void QDateTimeEditPrivate::clearCache() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QDateTimeEditPrivate10clearCacheEv(
    const QDateTimeEditPrivate *self) {
  self->QDateTimeEditPrivate::clearCache();
}

//  QStyle::SubControl QDateTimeEditPrivate::newHoverControl(const QPoint
//      &pos)
extern "C" Q_DECL_EXPORT
QStyle::SubControl ritual_own_ZN20QDateTimeEditPrivate15newHoverControlERK6QPoint(
    QDateTimeEditPrivate *self,
    const QPoint *pos) {
  return self->QDateTimeEditPrivate::newHoverControl(*pos);
}

//  void QDateTimeEditPrivate::updateEditFieldGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeEditPrivate23updateEditFieldGeometryEv(
    QDateTimeEditPrivate *self) {
  self->QDateTimeEditPrivate::updateEditFieldGeometry();
}

//  QVariant QDateTimeEditPrivate::getZeroVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QDateTimeEditPrivate14getZeroVariantEv(
    const QDateTimeEditPrivate *self) {
  return new QVariant(self->QDateTimeEditPrivate::getZeroVariant());
}

//  void QDateTimeEditPrivate::setRange(const QVariant &min, const QVariant
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDateTimeEditPrivate8setRangeERK8QVariantS2_(
    QDateTimeEditPrivate *self,
    const QVariant *min,
    const QVariant *max) {
  self->QDateTimeEditPrivate::setRange(*min, *max);
}

//  QString QDateTimeEditPrivate::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QDateTimeEditPrivate11displayTextEv(
    const QDateTimeEditPrivate *self) {
  return new QString(self->QDateTimeEditPrivate::displayText());
}

//  QDateTime QDateTimeEditPrivate::getMinimum(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_own_ZNK20QDateTimeEditPrivate10getMinimumERK9QTimeZone(
    const QDateTimeEditPrivate *self,
    const QTimeZone *zone) {
  return new QDateTime(self->QDateTimeEditPrivate::getMinimum(*zone));
}

//  QDateTime QDateTimeEditPrivate::getMaximum(const QTimeZone &zone) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_own_ZNK20QDateTimeEditPrivate10getMaximumERK9QTimeZone(
    const QDateTimeEditPrivate *self,
    const QTimeZone *zone) {
  return new QDateTime(self->QDateTimeEditPrivate::getMaximum(*zone));
}

//  QLocale QDateTimeEditPrivate::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_own_ZNK20QDateTimeEditPrivate6localeEv(
    const QDateTimeEditPrivate *self) {
  return new QLocale(self->QDateTimeEditPrivate::locale());
}

//  int QDateTimeEditPrivate::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QDateTimeEditPrivate14cursorPositionEv(
    const QDateTimeEditPrivate *self) {
  return self->QDateTimeEditPrivate::cursorPosition();
}
