//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgcssproperties_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtSvg/qtsvgglobal.h>
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#if QT_CONFIG(cssparser)
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgcssproperties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qxmlstream.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/private/qsvgcssproperties_p.h>
#include <QtGui/private/qguisvg_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 15, as local:qsvgcssproperties.cpp:parseCssClockValue
namespace {
inline int parseCssClockValue(QStringView str, bool *ok)
{
    int res = 0;
    int ms = 1000;
    str = str.trimmed();
    if (str.endsWith("ms"_L1)) {
        str.chop(2);
        ms = 1;
    } else if (str.endsWith("s"_L1)) {
        str.chop(1);
    } else {
        if (ok)
            *ok = false;
        return res;
    }
    double val = ms * str.toDouble(ok);
    if (ok) {
        if (val > std::numeric_limits<int>::min() && val < std::numeric_limits<int>::max())
            res = static_cast<int>(val);
        else
            *ok = false;
    }
    return res;
}
}  // namespace

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 40, as local:qsvgcssproperties.cpp:isTimeValue
namespace {
inline bool isTimeValue(QStringView str) {
    if (str.endsWith("ms"_L1))
        str.chop(2);
    else if (str.endsWith("s"_L1))
        str.chop(1);
    else
        return false;

    bool ok;
    Q_UNUSED(str.toDouble(&ok))
    return ok;
}
}  // namespace

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 53, as local:qsvgcssproperties.cpp:isIteration
namespace {
inline bool isIteration(QStringView str) {
    if (str == "infinite"_L1)
        return true;
    bool ok;
    Q_UNUSED(str.toDouble(&ok))
    return ok;
}
}  // namespace

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 61, as local:qsvgcssproperties.cpp:isDirection
namespace {
inline bool isDirection(QStringView str) {
    return str == "normal"_L1 || str == "reverse"_L1 || str.startsWith("alternate"_L1);
}
}  // namespace

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 65, as local:qsvgcssproperties.cpp:isTimingFunction
namespace {
inline bool isTimingFunction(QStringView str) {
    return str.startsWith("linear"_L1) || str.startsWith("ease"_L1)
           || str.startsWith("step"_L1) || str.startsWith("cubic-bezier"_L1);
}
}  // namespace

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 70, as local:qsvgcssproperties.cpp:isFillMode
namespace {
inline bool isFillMode(QStringView str) {
    return str == "none"_L1 || str == "forwards"_L1 || str == "backwards"_L1 || str == "both"_L1;
}
}  // namespace

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 74, as local:qsvgcssproperties.cpp:isPlayState
namespace {
inline bool isPlayState(QStringView str) {
    return str == "paused"_L1 || str =="running"_L1;
}
}  // namespace

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 218, as _ZN17QSvgCssProperties23shortHandtoLonghandFormE11QStringView
inline void QSvgCssProperties::shortHandtoLonghandForm(QStringView value)
{
    m_names.clear();
    m_durations.clear();
    m_delays.clear();
    m_iterationCounts.clear();
    m_directions.clear();
    m_timingFunctions.clear();
    m_fillModes.clear();
    m_playStates.clear();

    enum Property : uchar {
        Duration = 1,
        Delay = 1 << 1,
        IterationCount = 1 << 2,
        Direction = 1 << 3,
        TimingFunction = 1 << 4,
        FillMode = 1 << 5,
        PlayState = 1 << 6,
        Name = 1 << 7
    };

    const QList<QStringView> animations = value.split(QLatin1Char(';'), Qt::SkipEmptyParts);
    for (const QStringView &animation : animations) {
        uchar propertyFlag = 0;
        const QList<QStringView> animationProperties = animation.split(QLatin1Char(' '), Qt::SkipEmptyParts);
        for (const QStringView &property : animationProperties) {
            if (!(propertyFlag & Property::Duration) && isTimeValue(property)) {
                m_durations.append(property);
                propertyFlag |= Property::Duration;
            } else if (!(propertyFlag & Property::Delay) && isTimeValue(property)) {
                m_delays.append(property);
                propertyFlag |= Property::Delay;
            } else if (!(propertyFlag & Property::IterationCount) && isIteration(property)) {
                m_iterationCounts.append(property);
                propertyFlag |= Property::IterationCount;
            } else if (!(propertyFlag & Property::Direction) && isDirection(property)) {
                m_directions.append(property);
                propertyFlag |= Property::Direction;
            } else if (!(propertyFlag & Property::TimingFunction) && isTimingFunction(property)) {
                m_timingFunctions.append(property);
                propertyFlag |= Property::TimingFunction;
            } else if (!(propertyFlag & Property::FillMode) && isFillMode(property)) {
                m_fillModes.append(property);
                propertyFlag |= Property::FillMode;
            }  else if (!(propertyFlag & Property::PlayState)&& isPlayState(property)) {
                m_playStates.append(property);
                propertyFlag |= Property::PlayState;
            } else {
                m_names.append(property);
                propertyFlag |= Property::Name;
            }
        }
    }
}

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 80, as _ZN17QSvgCssPropertiesC1ERK20QXmlStreamAttributes
inline QSvgCssProperties::QSvgCssProperties(const QXmlStreamAttributes &attributes)
{
    QRegularExpression re(";| "_L1);
    for (int i = 0; i < attributes.size(); ++i) {
        const QXmlStreamAttribute &attribute = attributes.at(i);
        QStringView name = attribute.qualifiedName();
        if (name.isEmpty())
            continue;
        QStringView value = attribute.value();
        switch (name.at(0).unicode()) {

        case 'a':
            if (name == "animation"_L1)
                shortHandtoLonghandForm(value);
            if (name == "animation-name"_L1)
                m_names = value.split(re, Qt::SkipEmptyParts);
            if (name == "animation-duration"_L1)
                m_durations = value.split(re, Qt::SkipEmptyParts);
            if (name == "animation-delay"_L1)
                m_delays = value.split(re, Qt::SkipEmptyParts);
            if (name == "animation-iteration-count"_L1)
                m_iterationCounts = value.split(re, Qt::SkipEmptyParts);
            if (name == "animation-direction"_L1)
                m_directions = value.split(re, Qt::SkipEmptyParts);
            if (name == "animation-timing-function"_L1)
                m_timingFunctions = value.split(re, Qt::SkipEmptyParts);
            if (name == "animation-fill-mode"_L1)
                m_fillModes = value.split(re, Qt::SkipEmptyParts);
            if (name == "animation-play-state"_L1)
                m_playStates = value.split(re, Qt::SkipEmptyParts);
            break;

        case 'o':
            if (name == "offset-path"_L1)
                m_offsetPath = value;
            if (name == "offset-distance"_L1)
                m_offsetDistance = value;
            if (name == "offset-rotate"_L1)
                m_offsetRotate = value;
            break;

        default:
            break;
        }
    }
}

//  from ../qtsvg/src/svg/css/qsvgcssproperties.cpp, line 183, as _ZNK17QSvgCssProperties6offsetEv
inline QSvgOffsetProperty QSvgCssProperties::offset() const
{
    QSvgOffsetProperty offset;

    offset.path = QGuiSvg::parsePath(m_offsetPath);

    qsizetype index;
    Qt::CaseSensitivity cs = Qt::CaseInsensitive;
    if ((index = m_offsetRotate.indexOf("auto"_L1, 0, cs)) >= 0) {
        std::optional<qreal> angle = QGuiSvg::parseAngle(m_offsetRotate.sliced(index + 4));
        offset.rotateType = angle ? QtSvg::OffsetRotateType::AutoAngle :
                                QtSvg::OffsetRotateType::Auto;
        offset.angle = angle.value_or(0);
    } else if ((index = m_offsetRotate.indexOf("reverse"_L1, 0, cs)) >= 0) {
        std::optional<qreal> angle = QGuiSvg::parseAngle(m_offsetRotate.sliced(index + 7));
        offset.rotateType = angle ? QtSvg::OffsetRotateType::ReverseAngle :
                                QtSvg::OffsetRotateType::Reverse;
        offset.angle = angle.value_or(0);
    } else {
        std::optional<qreal> angle = QGuiSvg::parseAngle(m_offsetRotate);
        offset.rotateType = angle ? QtSvg::OffsetRotateType::Angle :
                                QtSvg::OffsetRotateType::Auto;
        offset.angle = angle.value_or(0);
    }

    QGuiSvg::LengthType type;
    bool *ok = nullptr;
    offset.distance= QGuiSvg::parseLength(m_offsetDistance, &type, ok);
    if (type == QGuiSvg::LengthType::LT_PERCENT) {
        offset.distance = offset.distance / 100.0;
    }

    return offset;
}
//  -----------------------------------------------------------------------

//  QSvgCssProperties::QSvgCssProperties(const QXmlStreamAttributes
//      &attributes)
extern "C" Q_DECL_EXPORT
QSvgCssProperties *ritual_ZN17QSvgCssPropertiesC1ERK20QXmlStreamAttributes(
    const QXmlStreamAttributes *attributes) {
  return new QSvgCssProperties(*attributes);
}

//  QSvgOffsetProperty QSvgCssProperties::offset() const
extern "C" Q_DECL_EXPORT
QSvgOffsetProperty *ritual_ZNK17QSvgCssProperties6offsetEv(
    const QSvgCssProperties *self) {
  return new QSvgOffsetProperty(self->offset());
}

//  QSvgCssProperties::~QSvgCssProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgCssPropertiesD1Ev(QSvgCssProperties *self) {
  delete self;
}

#endif  // QT_CONFIG(cssparser)
